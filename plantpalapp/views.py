from django.shortcuts import render, get_object_or_404

from .models import Plant

def index(request):
    plants = Plant.objects.order_by("name")
    return render(request, "plantpalapp/index.html", { "plants": plants })

def show_plant(request, plant_id):
    plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, "plantpalapp/show_plant.html", { "plant": plant })
