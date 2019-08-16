from django.urls import path

from . import views

urlpatterns = [
    # ex: /plants
    path('', views.index, name='index'),
]
