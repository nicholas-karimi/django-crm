from django.urls import path
from .views import (leads_list, lead_detail,
                         lead_create, lead_update, delete_lead)

# namespaces
app_name = 'leads'

urlpatterns = [
    path('', leads_list, name='leads'),
    path('create/', lead_create, name='new-lead'),
    path('<int:pk>/', lead_detail, name='lead'),
    path('update/<int:pk>/', lead_update, name='update-lead'),
    path('delete/<int:pk>/', delete_lead, name='delete-lead'),

]
