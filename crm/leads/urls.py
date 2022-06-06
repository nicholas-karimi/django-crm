from django.urls import path
from .views import (LeadListView, leadDetailView,
                         LeadCreateView, lead_update, LeadUpdateView,LeadDeleteView, delete_lead)

# namespaces
app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='leads'),
    path('create/', LeadCreateView.as_view(), name='new-lead'),
    path('<int:pk>/', leadDetailView.as_view(), name='lead'),
    path('update/<int:pk>/', LeadUpdateView.as_view(), name='update-lead'),
    path('delete/<int:pk>/', LeadDeleteView.as_view(), name='delete-lead'),

]
