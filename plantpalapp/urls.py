from django.urls import path

from . import views

urlpatterns = [
    # ex: /plants
    path('', views.index, name='index'),
    # ex: /plants/5/
    path('<int:plant_id>/', views.show_plant, name='plant'),
]
