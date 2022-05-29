from django.urls import path
from .views import leads_list, lead_detail, lead_create

# namespaces
app_name = 'leads'

urlpatterns = [
    path('', leads_list, name='leads'),
    path('create/', lead_create, name='new-lead'),
    path('<int:pk>/', lead_detail, name='lead'),
]