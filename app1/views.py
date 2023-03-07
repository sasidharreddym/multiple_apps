from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def function1_app1(request):
    return HttpResponse('<h1>first function in application 1</h1>')

def function2_app1(request):
    return HttpResponse('<h1>second function of application 1</h1>')

def function3_app1(request):
    return HttpResponse('<h1>third function of application 1</h1>')