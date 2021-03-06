# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Agenthostname(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20)  # Field name made lowercase.
    bpaagentname = models.CharField(db_column='BpaAgentName', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AgentHostName'
        unique_together = (('name', 'bpaagentname'),)


class Client(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Client'


class Clientworkflow(models.Model):
    clientid = models.ForeignKey(Client, models.DO_NOTHING, db_column='ClientId', primary_key=True)  # Field name made lowercase.
    workflowid = models.ForeignKey('Workflow', models.DO_NOTHING, db_column='WorkflowId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ClientWorkflow'
        unique_together = (('clientid', 'workflowid'), ('workflowid', 'clientid'),)


class Environment(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Environment'


class Result(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    agentid = models.ForeignKey(Agenthostname, models.DO_NOTHING, db_column='AgentId')  # Field name made lowercase.
    executiondate = models.DateTimeField(db_column='ExecutionDate')  # Field name made lowercase.
    clientid = models.ForeignKey(Client, models.DO_NOTHING, db_column='ClientId')  # Field name made lowercase.
    environmentid = models.ForeignKey(Environment, models.DO_NOTHING, db_column='EnvironmentId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Result'


class Resultdetail(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    resultid = models.ForeignKey(Result, models.DO_NOTHING, db_column='ResultId')  # Field name made lowercase.
    testid = models.ForeignKey('Test', models.DO_NOTHING, db_column='TestId')  # Field name made lowercase.
    starttime = models.DateTimeField(db_column='StartTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime')  # Field name made lowercase.
    stateid = models.ForeignKey('State', models.DO_NOTHING, db_column='StateId')  # Field name made lowercase.
    triggerid = models.ForeignKey('Trigger', models.DO_NOTHING, db_column='TriggerId')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultDetail'


class Resultdetailtext(models.Model):
    resultdetailid = models.ForeignKey(Resultdetail, models.DO_NOTHING, db_column='ResultDetailId', primary_key=True)  # Field name made lowercase.
    details = models.TextField(db_column='Details', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ResultDetailText'


class State(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'State'


class Task(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    workflowid = models.ForeignKey('Workflow', models.DO_NOTHING, db_column='WorkflowId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Task'
        unique_together = (('name', 'workflowid'),)


class Technology(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Technology'


class Test(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    taskid = models.ForeignKey(Task, models.DO_NOTHING, db_column='TaskId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Test'
        unique_together = (('name', 'taskid'),)


class Trigger(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Trigger'


class Workflow(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    technologyid = models.ForeignKey(Technology, models.DO_NOTHING, db_column='TechnologyId')  # Field name made lowercase.
    name = models.CharField(db_column='Name', unique=True, max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Workflow'
