from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from core.models import Category
from core.serializers import CategorySerializer
# Create your views here.


def web_site(request: HttpResponse) -> HttpRequest:
    return HttpResponse("Hello World")
    


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer