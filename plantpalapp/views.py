from django.shortcuts import render

from django.http import HttpResponse

from .models import Plant

def index(request):
    plants = Plant.objects.order_by("name")
    context = { "plants": plants }
    return render(request, "plantpalapp/index.html", context)
