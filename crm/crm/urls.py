from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from leads.views import index, RegistrationView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('leads/', include('leads.urls', namespace='leads')),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', RegistrationView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),


]

if settings.DEBUG:
    static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)