from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import register
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('registro/', register, name="registro"),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name="logout"),
]