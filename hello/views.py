from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello, World!<br>Updated on GitHub and reflected automatically through Azure. Yay!")
