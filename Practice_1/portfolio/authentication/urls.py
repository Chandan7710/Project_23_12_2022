from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.authlogin, name = 'login'),
    path('registration/', views.authregistration, name = 'registration'),
    path('forgetpassword/', views.forgetpassword, name = 'forgetpassword'),
    path('logout/', views.authlogout, name = 'logout'),
]
