from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from rest_framework import views, status, viewsets, generics
from .serializers import *
from .models import *
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.db.models import Count, Q, Case, CharField, Value, When
import json
from rest_framework.pagination import PageNumberPagination
from django.core.paginator import Paginator
from django.apps import apps
from django.utils import timezone
import datetime
from itertools import chain
from django.db import connection
from django.db.models import Max
from django.db.models import F
from django.db.models import When, Case, Sum, IntegerField

# Function to filter the latest of each test and return their execution dates as a list
def get_execution_date_list():
    # Get queryset of Max execution date grouped by workflow (bcz each workflow may have different execution date)
    max_date_queryset = Result.objects.values('clientid','workflowid').annotate(max_date=Max('executiondate'))
    # get a list of Max excecution dates of all workflows
    execution_date_list=[]
    for r in max_date_queryset:
        execution_date_list.append(r['max_date'])
    return execution_date_list

# Function that returns state counts for specific client, technology, workflow, state, and test parameters.
# Need more data to validate the SQL code.
class get_state_counts():
    def get(self, request, qryset):
        # Get all request parameters.
        parameter_dict = request.GET
        # Dictionary to convert keys into model's attributes
        dict = {
            "client": "resultid__clientid__name",
            "technology": "testid__taskid__workflowid__technologyid__name",
            "workflow": "testid__taskid__workflowid__name",
            "state": "stateid__name",
            "test" : "testid__name"
            }
        # Add parameter conditions to queryset using parameter key and value.
        for key in parameter_dict:
            qryset = qryset.filter(**{dict[key]: parameter_dict.__getitem__(key)})
        # Add aggregate count function for states.
        qryset = qryset.annotate(
            Total=Count(F('stateid')),
            Success=Sum(Case(When(stateid=28, then=1), default=0, output_field=IntegerField())),
            Warning=Sum(Case(When(stateid=29, then=1), default=0, output_field=IntegerField())),
            Failed=Sum(Case(When(stateid=27, then=1), default=0, output_field=IntegerField())), 
            )
        return qryset

# API that returns a specific test along with its details, the test ID should be passed in the URL param"
class get_test_by_id(generics.ListAPIView):
    serializer_class = ResultdetailSerializer
    def get_queryset(self):
        test = self.request.query_params.get('testid', None)
        try:
            queryset= Resultdetail.objects.filter(resultid__executiondate__in=get_execution_date_list(), testid__id=test)
            #print(queryset.query)
            pagination_class = PageNumberPagination
            return queryset
        except Resultdetail.DoesNotExist:
            raise Http404

# API that returns latest tests with optional client, workflow, technology, and state parameters.
class get_test_list(generics.ListAPIView):
    serializer_class = ResultdetailSerializerTests
    def get_queryset(self):
        # Get all request parameters.
        parameter_dict = self.request.GET
        # Filter query set by latest execution date.
        queryset = Resultdetail.objects.select_related('resultid','testid','stateid','triggerid').filter(resultid__executiondate__in=get_execution_date_list())
        #print(queryset.query)
        # Dictionary to convert keys into model's attributes
        dict = {
            "client": "resultid__clientid__name",
            "technology": "testid__taskid__workflowid__technologyid__name",
            "workflow": "testid__taskid__workflowid__name",
            "state": "stateid__name",
            "testid" : "testid"
            }
        # Add parameter conditions to queryset using parameter key and value.
        for key in parameter_dict:
            if key =='offset' or key=='limit':
                pass
            else:
                queryset = queryset.filter(**{dict[key]: parameter_dict.__getitem__(key)})
        # Put the records in order, an put them in a list to avoid gorup_by restriction 
        queryset = list(queryset.annotate(
            priority=Case(
                When(stateid=27, then=Value('1')),
                When(stateid=29, then=Value('2')),
                When(stateid=28, then=Value('3')),
                default=Value('4'), output_field=CharField(),),
            ).order_by('priority'))
        #print(queryset.query)
        pagination_class = PageNumberPagination
        return queryset

# API that returns state counts for all clients.
# Need more data to validate the SQL code.
class get_client_state_counts(generics.ListAPIView):
    def get(self, request):
        # Join needed fields and rename to integrate dynamic filtering of parameters.
        queryset = Resultdetail.objects.filter(resultid__executiondate__in=get_execution_date_list()).select_related('resultid','testid','stateid','triggerid').values(client=F('resultid__clientid__name'))  
         # Call the state counts method to get the counts
        queryset = get_state_counts.get(self, request, queryset)
        return Response(queryset)

# API that returns technologies' state counts for specific client.
# Need more data to validate the SQL code.
class get_technology_state_counts(generics.ListAPIView):
    def get(self, request):
        # Join needed fields and rename to integrate dynamic filtering of parameters.
        queryset = Resultdetail.objects.filter(resultid__executiondate__in=get_execution_date_list()).select_related('resultid','testid','stateid','triggerid').values(technology = F('testid__taskid__workflowid__technologyid__name'))  
         # Call the state counts method to get the counts
        queryset = get_state_counts.get(self, request, queryset)
        return Response(queryset)

# API that returns Workflows' state counts for specific client and technology.
# Need more data to validate the SQL code.
class get_workflow_state_counts(generics.ListAPIView):
    def get(self, request):
        # Get queryset of Max execution date grouped by workflow (bcz each workflow may have different execution date)
        max_date_queryset = Result.objects.values('clientid','technologyid','workflowid').annotate(max_date=Max('executiondate'))
        # get a list of Max excecution dates of all workflows
        execution_date_list=[]
        for r in max_date_queryset:
            execution_date_list.append(r['max_date'])
        
        queryset = Resultdetail.objects.filter(resultid__executiondate__in=execution_date_list).select_related('resultid','testid','stateid','triggerid').values(workflow = F('testid__taskid__workflowid__name'))  
         # Call the state counts method to get the counts
        queryset = get_state_counts.get(self, request, queryset)
        return Response(queryset)