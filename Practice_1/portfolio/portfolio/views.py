from django.http import HttpResponse
from django.shortcuts import render


def demo_fun(request):
    return render(request, 'demo.html')

    