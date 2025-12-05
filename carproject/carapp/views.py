from django.shortcuts import render
from .models import Car

# Create your views here.
def showcars(request):
    cars = Car.objects.all() # fetch all cars you have in your db
    return render(request, "index.html", {"car": cars})