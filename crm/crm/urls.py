from django.contrib import admin
from django.urls import path, include
from leads.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('leads/', include('leads.urls', namespace='leads')),

]
