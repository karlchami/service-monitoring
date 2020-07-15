from django.test import TestCase
from django.utils.timezone import make_aware
from catalog.models import *
from django.utils import timezone
import random


# Verifying label name, max lengths, and values of some of the key fields in this model.
# This is the most that can be done for testing a read-only model.

# set as global so they can be accessed from other functions for testing
clients = ['CIBC', 'DESJ', 'TD', 'INFOS', 'LOBLAWS', 'CMZ', 'CDS', 'COT', 'COO']
technologies = ['Genesys', 'GenX', 'Cisco', 'XYZ']
environments = ['Prod', 'Lab A', 'Lab B', 'Lab C', 'Pre Prod']
states = ['Passed', 'Failed', 'Warning']
trigger = ['Auto', 'Manual']
agenthostname = ['PCBEVDAPRGTLS01', 'other']
bpaagentName = ['CIBC - PCBEVDAPRGTLS01', 'other - other']

class Dash_TestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        now = timezone.now() #to get the current date and time
        Client.objects.create(id =1 ,name=clients[0])
        Technology.objects.create(id=1, name=technologies[0])
        Environment.objects.create(id=1, name=environments[0])
        Agenthostname.objects.create(id=1, name=agenthostname[0], bpaagentname=bpaagentName[0])
        agentId=Agenthostname.objects.get(id=1)
        clientId=Client.objects.get(id=1)
        environmentId=Environment.objects.get(id=1)
        technologyId=Technology.objects.get(id=1)
        environmentId=Environment.objects.get(id=1)
        Workflow.objects.create(id =1 ,name='WORKF 1', technologyid=technologyId)
        WorkflowId=Workflow.objects.get(id=1)

        Result.objects.create(id =1 ,agentid=agentId, executiondate='2020-06-16 00:47:25', clientid=clientId, environmentid=environmentId, workflowid=WorkflowId ,technologyid=technologyId)
        Trigger.objects.create(id =1 ,name=trigger[0])

        workflowId=Workflow.objects.get(id=1)
        resultId=Result.objects.get(id=1)

        Task.objects.create(id =1 ,name='Task 1', workflowid=workflowId)

        taskId=Task.objects.get(id=1)

        Test.objects.create(id =1 ,name='test 1', taskid=taskId)
        State.objects.create(id =1 ,name=states[0])

        testId=Test.objects.get(id=1)
        triggerId=Trigger.objects.get(id=1)
        stateId=State.objects.get(id=1)

        Resultdetail.objects.create(id =1 ,resultid=resultId, testid=testId,starttime=now, endtime=now,stateid=stateId,triggerid=triggerId)

        resultdetailId=Resultdetail.objects.get(id=1)

        Resultdetailtext.objects.create(resultdetailid=resultdetailId, details='123 details')
        Clientworkflow.objects.create(clientid=clientId, workflowid=workflowId)

    def test_clientName_max_length(self):
        component = Client.objects.get(id=1)
        max_length = component._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_clientName(self):
        component = Client.objects.get(id=1)
        expected_object_name = component.name
        self.assertEquals(expected_object_name, clients[0])

    def test_Agenthostname_max_length(self):
        component = Agenthostname.objects.get(id=1)
        max_length = component._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_AgenthostnametName(self):
        component = Agenthostname.objects.get(id=1)
        expected_object_name = component.name
        self.assertEquals(expected_object_name, agenthostname[0])
    
    def test_Agenthostnamet_bpaName(self):
        component = Agenthostname.objects.get(id=1)
        expected_object_name = component.bpaagentname
        self.assertEquals(expected_object_name, bpaagentName[0])

    def test_Environment_max_length(self):
        component = Environment.objects.get(id=1)
        max_length = component._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_EnvironmentName(self):
        component = Environment.objects.get(id=1)
        expected_object_name = component.name
        self.assertEquals(expected_object_name, environments[0])


    def test_Result(self):
        component = Result.objects.get(id=1)
        expected_object_name =  component.executiondate.strftime('%Y-%m-%d')
        self.assertEquals(expected_object_name, '2020-06-16')

    def test_Resultdetail_startT(self):
        component = Resultdetail.objects.get(id=1)
        expected_object_name = component.starttime.strftime('%Y-%m-%d')
        # .strf to compare the date only, because we will definitely have different time after running the test (like 1 second delay)
        self.assertEquals(expected_object_name, timezone.now().strftime('%Y-%m-%d'))

    def test_Resultdetail_endT(self):
        component = Resultdetail.objects.get(id=1)
        expected_object_name = component.endtime.strftime('%Y-%m-%d')
        # .strf to compare the date only, because we will definitely have different time after running the test (like 1 second delay)
        self.assertEquals(expected_object_name, timezone.now().strftime('%Y-%m-%d'))

    def test_Resultdetailtext(self):
        component = Resultdetailtext.objects.get(resultdetailid=1)
        expected_object_name = component.details
        self.assertEquals(expected_object_name, '123 details')

    def test_Task_max_length(self):
        component = Task.objects.get(id=1)
        max_length = component._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_Task(self):
        component = Task.objects.get(id=1)
        expected_object_name = component.name
        self.assertEquals(expected_object_name, 'Task 1')

    def test_Technology_max_length(self):
        component = Technology.objects.get(id=1)
        max_length = component._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_Technology(self):
        component = Technology.objects.get(id=1)
        expected_object_name = component.name
        self.assertEquals(expected_object_name, technologies[0])

    def test_Test_max_length(self):
        component = Test.objects.get(id=1)
        max_length = component._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_Test(self):
        component = Test.objects.get(id=1)
        expected_object_name = component.name
        self.assertEquals(expected_object_name, 'test 1')

    def test_Trigger_max_length(self):
        component = Trigger.objects.get(id=1)
        max_length = component._meta.get_field('name').max_length
        self.assertEquals(max_length, 20)

    def test_Trigger(self):
        component = Trigger.objects.get(id=1)
        expected_object_name = component.name
        self.assertEquals(expected_object_name, trigger[0])

    def test_Workflow_max_length(self):
        component = Workflow.objects.get(id=1)
        max_length = component._meta.get_field('name').max_length
        self.assertEquals(max_length, 50)

    def test_Workflow(self):
        component = Workflow.objects.get(id=1)
        expected_object_name = component.name
        self.assertEquals(expected_object_name, 'WORKF 1')