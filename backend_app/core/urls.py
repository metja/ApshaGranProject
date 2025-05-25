from django.urls import path
from core.views import web_site

urlpatterns = [
    path("", web_site, name="web-site"),
]



app_name = "core"