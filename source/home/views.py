from django.shortcuts import render, get_object_or_404

from .models import Sports


# Create your views here.
def home(request):
    photo_sport = Sports.objects.all()
    return render(request, 'home/home.html', {'photo_sport': photo_sport})


def details_sport(request, slug):
    sport = get_object_or_404(Sports, slug=slug)
    return render(request, 'home/details_sport.html', {'sport': sport})
