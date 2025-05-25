from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.


def web_site(request: HttpResponse) -> HttpRequest:
    return HttpResponse("Hello World")
    
    