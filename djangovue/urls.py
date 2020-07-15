from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_test_by_id/', views.get_test_by_id.as_view(), name='get_test_by_id'),
    path('get_test_list/', views.get_test_list.as_view(), name='get_test_list'),
    path('get_client_state_counts/', views.get_client_state_counts.as_view(), name='get_client_state_counts'),
    path('get_technology_state_counts/', views.get_technology_state_counts.as_view(), name='get_technology_state_counts'),
    path('get_workflow_state_counts/', views.get_workflow_state_counts.as_view(), name='get_workflow_state_counts')
]