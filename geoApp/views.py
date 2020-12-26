from django.shortcuts import render
from .models import Location


def index(request):
    locations = Location.objects.all()
    return render(request, 'index.html', {'locations': locations})
