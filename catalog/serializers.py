from abc import ABC
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from rest_framework import serializers
from djoser.conf import settings
from .models import *


class ClientworkflowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientworkflow
        fields = '__all__'
        depth = 2

class ResultdetailtextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resultdetailtext
        fields = '__all__'

class ResultdetailSerializerTests(serializers.ModelSerializer):
    test_id = serializers.CharField(read_only=True, source='testid.id')
    test_name = serializers.CharField(read_only=True, source='testid.name')
    state = serializers.CharField(read_only=True, source='stateid.name')

    class Meta:
        model = Resultdetail
        fields= ('test_id','test_name','state')

class ResultdetailSerializer(serializers.ModelSerializer):
    result_detail = ResultdetailtextSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Resultdetail
        fields = '__all__'
        depth = 2

class ResultSerializer(serializers.ModelSerializer):
    resultDetail_result = ResultdetailSerializer(many=True, read_only=True)
    class Meta:
        model = Result
        fields = '__all__'

class AgenthostnameSerializer(serializers.ModelSerializer):
    result_agent = ResultSerializer(many=True, read_only=True)
    class Meta:
        model = Agenthostname
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    result_client = ResultSerializer(many=True, read_only=True)
    clientworkflow_client = ClientworkflowSerializer(many=True, read_only=True)
    class Meta:
        model = Client
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    resultDetail_test = ResultdetailSerializer(many=True, read_only=True)
    class Meta:
        model = Test
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    task_test = TestSerializer(many=True, read_only=True)
    class Meta:
        model = Task
        fields = '__all__'

class WorkflowSerializer(serializers.ModelSerializer):
    clientworkflow_workflow = ClientworkflowSerializer(many=True, read_only=True)
    workflow_Task = TaskSerializer(many=True, read_only=True)
    class Meta:
        model = Workflow
        fields = '__all__'

class EnvironmentSerializer(serializers.ModelSerializer):
    result_environment = ResultSerializer(many=True, read_only=True)
    class Meta:
        model = Environment
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    resultDetail_state = ResultdetailSerializer(many=True, read_only=True)
    class Meta:
        model = State
        fields = '__all__'

class TechnologySerializer(serializers.ModelSerializer):
    tech_workflow = WorkflowSerializer(many=True, read_only=True)
    class Meta:
        model = Technology
        fields = '__all__'

class TriggerSerializer(serializers.ModelSerializer):
    resultDetail_trigger = ResultdetailSerializer(many=True, read_only=True)
    class Meta:
        model = Trigger
        fields = '__all__'

