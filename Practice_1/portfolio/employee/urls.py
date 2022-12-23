from django.urls import path
from employee import views

urlpatterns = [
    path('new/', views.employee),
    path('profile/', views.profile, name = 'profile'),
]
