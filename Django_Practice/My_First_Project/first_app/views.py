from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Musician, Album
from first_app import forms

# Create your views here.


def contact(request):
    return HttpResponse("<h1>This is contact page</h1> <a href='/about/'>About</a> | <a href='/layout/'>Layout</a> ")

def about(request):
    return HttpResponse("<h1>This is about page</h1> <a href='/'>Contact</a> | <a href='/layout/'>Layout</a> ")

def layout(request):
    return HttpResponse("<h1>This is layout page</h1> <a href='/'>Contact</a> | <a href='/about/'>About</a> ")

def index(request):
    # SELECT * FROM MUSICIAN ORDER BY first_name
    musician_list = Musician.objects.order_by('first_name')
    dict = {'text_1': "This is a list of musician",
            'musician': musician_list}
    return render(request, 'first_app/index.html', context = dict)

def form(request):
    new_form = forms.user_form()
    dict1 = {'test_form': new_form,
             'heading_1': "This is from user django library"}
    
    if request.method == 'POST':
        new_form = forms.user_form(request.POST)
        
        if new_form.is_valid():
            user_name = new_form.cleaned_data['user_name']
            user_dob = new_form.cleaned_data['user_dob']
            user_email = new_form.cleaned_data['user_email']
            
            dict1.update({'user_name':user_name})
            dict1.update({'user_dob':user_dob})
            dict1.update({'user_email':user_email})
            dict1.update({'form_submited':"Yes"})
    
    return render(request, 'first_app/form.html', context = dict1)

def form1(request):
    new_form = forms.user_form1()
    dict1 = {'test_form': new_form,
             'heading_1': "This is from user django library"}
    
    if request.method == 'POST':
        new_form = forms.user_form1(request.POST)
        
        if new_form.is_valid():
        
            dict1.update({'boolean_field': new_form.cleaned_data['boolean_field']})
            dict1.update({'char_field': new_form.cleaned_data['char_field']})
            dict1.update({'choice_field': new_form.cleaned_data['choice_field']})
            dict1.update({'choice_field1': new_form.cleaned_data['choice_field1']})
            dict1.update({'form_submited': "Yes"})
    
    return render(request, 'first_app/form1.html', context = dict1)


def form2(request):
    new_form = forms.user_form2()
    dict1 = {'test_form': new_form,
             'heading_1': "This is from user django library"}
    
    if request.method == 'POST':
        new_form = forms.user_form2(request.POST)
        dict1.update({'test_form':new_form})
        
        if new_form.is_valid():
        
            # dict1.update({'char_field': new_form.cleaned_data['char_field']})
            dict1.update({'number_field': new_form.cleaned_data['number_field']})
            dict1.update({'form_submited': "Yes"})
    
    return render(request, 'first_app/form2.html', context = dict1)


def form3(request):
    new_form = forms.user_form3()
    dict1 = {'test_form': new_form,
             'heading_1': "This is from user django library"}
    
    if request.method == 'POST':
        new_form = forms.user_form3(request.POST)
        dict1.update({'test_form':new_form})
        
        if new_form.is_valid():
        
            dict1.update({'number_field': 'Fields Match !!'})
            dict1.update({'form_submited': "Yes"})
    
    return render(request, 'first_app/form3.html', context = dict1)


def data_form(request):
    new_form = forms.MusicianForm()
    
    if request.method == 'POST':
        new_form = forms.MusicianForm(request.POST)
        
        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)
        
    dict2 = {'test_form': new_form,
             'heading_1': 'Add New Musician'}

    return render(request, 'first_app/form4.html', context = dict2)