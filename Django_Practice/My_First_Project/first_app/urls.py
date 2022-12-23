from django.urls import path
from django.conf.urls import url
from first_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('form/', views.form, name='form'),
    path('form1/', views.form1, name='form1'),
    path('form2/', views.form2, name='form2'),
    path('form2/', views.form2, name='form2'),
    path('form3/', views.form3, name='form3'),
    path('data_form/', views.data_form, name='data_form'),
]
