from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import web_site, CategoryViewSet


router = DefaultRouter()
router.register('categories', CategoryViewSet)

urlpatterns = [
    path("", web_site, name="web-site"),
    path('', include(router.urls)),
]



app_name = "core"