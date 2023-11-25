from django.urls import path
from django.contrib.auth import views as auth_views
from login.views import Credencial

urlpatterns = [
  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='Login'),
  path('logout/', auth_views.LogoutView.as_view(), name='Logout'),
  path('credencial/', Credencial.as_view(), name='Credencial'),
]