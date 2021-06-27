from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, World!\nThis changed is to chekc behaviours on Azure app service. Yay!")
