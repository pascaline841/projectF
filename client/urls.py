from django.urls import path
from .views import multiple_databases


app_name = "client"

urlpatterns = [
    path("", multiple_databases, name='index')
]
