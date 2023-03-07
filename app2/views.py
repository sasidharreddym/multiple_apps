from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first_app2(request):
    return HttpResponse('<h3><marquee>first function of application 2</marquee></h3>')

def second_app2(request):
    return HttpResponse('<h2><marquee>second function of application 2</marquee></h2>')

def third_app2(request):
    return HttpResponse('<h2><marquee>third function of application 2</marquee></h2>')