from django.shortcuts import render, get_object_or_404
from .models import OffresTickets


# Create your views here.
def billetterie(request):
    billet = OffresTickets.objects.all()
    return render(request, 'tickets/billetterie.html', {'billet': billet})


def details_billet(request, slug):
    detail_billet = get_object_or_404(OffresTickets, slug=slug)
    return render(request, 'tickets/details_billet.html', {'details_billet': detail_billet})
