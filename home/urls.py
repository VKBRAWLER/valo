from django.urls import path
from . import views

#url config
urlpatterns = [
    path('', views.index, name='index'),
]
