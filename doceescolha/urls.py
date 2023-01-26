from django.urls import path

from doceescolha.views import home

urlpatterns = [
    path('', home)
]
