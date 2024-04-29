from django.contrib.auth.decorators import login_required
from django.forms import formset_factory
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .cart import Cart
from .forms import SoloForm, DuoForm, FamilleForm, CreditCardHolderForm
from .models import Solo, Duo, Famille
from tickets.models import OffresTickets


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa




# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    cart_tickets = cart.get_cart_tickets() # Liste des tickets du panier
    cart_items = cart.get_cart_items() # dictionnaire du panier utilisateur avec la quantité du ticket et le choix de sport
    cart_total = cart.get_cart_total()
    return render(request, 'cart/cart_summary.html', {'tickets': cart_tickets, 'cart_items': cart_items,
                                                      'cart_total': cart_total})


def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        ticket_id = request.POST.get('ticket_id')
        ticket_qty = request.POST.get('ticket_qty')
        sport_choice = request.POST.get('sport_choice')

        cart_qty = cart.__len__()
        cart.add(product_id=ticket_id, ticket_quantity=ticket_qty, sport_choice=sport_choice)

        response = JsonResponse({'cart_qty': cart_qty})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        ticket_id = request.POST.get('ticket_id')
        ticket_qty = request.POST.get('ticket_qty')
        sport_choice = request.POST.get('sport_choice')

        cart_qty = cart.__len__()

        cart.update(product_id=ticket_id, ticket_quantity=ticket_qty, sport_choice=sport_choice)

        response = JsonResponse({'cart_qty': cart_qty})
        return response


def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        ticket_id = request.POST.get('ticket_id')

        cart.delete(product_id=ticket_id)

        response = JsonResponse({'ticket id': ticket_id})
        return response


@login_required
def ticket_user_info(request):
    cart = Cart(request)
    extra_solo, extra_duo, extra_famille = cart.ticket_extra()
    sport_ticket_solo, sport_ticket_duo, sport_ticket_famille = cart.sport_choice()

    solo = formset_factory(SoloForm, extra=extra_solo)
    duo = formset_factory(DuoForm, extra=extra_duo)
    famille = formset_factory(FamilleForm, extra=extra_famille)

    if request.method == 'POST':
        formsolo = solo(request.POST, request.FILES, prefix='solo')
        formduo = duo(request.POST, request.FILES, prefix='duo')
        formfamille = famille(request.POST, request.FILES, prefix='famille')

        if all([formsolo.is_valid(), formduo.is_valid(), formfamille.is_valid()]):
            for form in [formsolo, formduo, formfamille]:
                for fm in form:
                    ticket = fm.save(commit=False)
                    ticket.user = request.user
                    ticket.cart = cart.get_cart_items()

                    if form == formsolo:
                        ticket.sport_choice = sport_ticket_solo
                    elif form == formduo:
                        ticket.sport_choice = sport_ticket_duo
                    else:
                        ticket.sport_choice = sport_ticket_famille
                    ticket.save()
        return redirect('card-holder')
    else:

        formsolo = solo(prefix='solo')
        formduo = duo(prefix='duo')
        formfamille = famille(prefix='famille')

    return render(request, 'cart/ticket_user_info.html', {'formsolo': formsolo, 'formduo': formduo,
                                                                                'formfamille': formfamille})


@login_required
def credit_card_holder_info(request):
    cart = Cart(request)
    card_info = CreditCardHolderForm()

    if request.method == 'POST':
        card_info = CreditCardHolderForm(request.POST)

        if card_info.is_valid():
            card = card_info.save(commit=False)
            card.total_price = cart.get_cart_total()
            card.save()
            cart.delete_cart()
            return redirect('user-ticket')
    else:
        card_info = CreditCardHolderForm()

    return render(request, 'cart/credit_card_holder_info.html', {'card_info': card_info})


@login_required
def display_user_ticket(request):
    img = OffresTickets.objects.get(pk=1)
    ticket_solo = Solo.objects.filter(user_id=request.user.id)
    ticket_duo = Duo.objects.filter(user_id=request.user.id)
    ticket_famille = Famille.objects.filter(user_id=request.user.id)
    return render(request, 'cart/user_ticket.html', {'ticket_solo': ticket_solo, 'ticket_duo': ticket_duo,
                                                     'ticket_famille': ticket_famille, 'img': img})
