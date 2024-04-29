from tickets.models import OffresTickets


class Cart:
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def __len__(self):
        return len(self.cart)

    def add(self, product_id, ticket_quantity, sport_choice):
        ticket_id = str(product_id)
        ticket_qty = int(ticket_quantity)
        sport_choice = str(sport_choice)

        if ticket_id in self.cart:
            pass
        else:
            self.cart[ticket_id] = {'ticket_qty': ticket_qty, 'sport_choice': sport_choice}
        self.session.modified = True

    def get_cart_tickets(self):
        tickets = OffresTickets.objects.filter(id__in=self.cart.keys())
        return tickets

    def get_cart_items(self):
        cart_items = self.cart.items()
        return cart_items

    def update(self, product_id, ticket_quantity, sport_choice):
        ticket_id = str(product_id)
        ticket_qty = int(ticket_quantity)
        sport_choice = str(sport_choice)

        if ticket_id in self.cart:
            self.cart[ticket_id]['ticket_qty'] = ticket_qty
            self.cart[ticket_id]['sport_choice'] = sport_choice
        self.session.modified = True

    def delete(self, product_id):
        ticket_id = product_id

        if ticket_id in self.cart:
            del self.cart[ticket_id]
        self.session.modified = True

    def get_cart_total(self):
        total = 0
        cart_ids = self.cart.keys()
        tickets = OffresTickets.objects.filter(id__in=cart_ids)

        for ticket in tickets:
            for key, value in self.cart.items():
                for ky, val in value.items():

                    if int(key) == ticket.id:
                        if ky == 'ticket_qty':
                            total += (ticket.price * val)
        return total

    def ticket_extra(self):
        extra_solo = extra_duo = extra_famille = 0

        for key, value in self.cart.items():

            ticket = OffresTickets.objects.get(id=int(key))
            if int(key) == ticket.id and ticket.number_of_place == 1:
                extra_solo = value["ticket_qty"]

            if int(key) == ticket.id and ticket.number_of_place == 2:
                extra_duo = value["ticket_qty"] * 2

            if int(key) == ticket.id and ticket.number_of_place == 4:
                extra_famille = value["ticket_qty"] * 4

        return extra_solo, extra_duo, extra_famille

    def sport_choice(self):
        sport_ticket_solo = sport_ticket_duo = sport_ticket_famille = ""

        for key, value in self.cart.items():

            ticket = OffresTickets.objects.get(id=int(key))
            if int(key) == ticket.id and ticket.number_of_place == 1:
                sport_ticket_solo = value["sport_choice"]

            if int(key) == ticket.id and ticket.number_of_place == 2:
                sport_ticket_duo = value["sport_choice"]

            if int(key) == ticket.id and ticket.number_of_place == 4:
                sport_ticket_famille = value["sport_choice"]

        return sport_ticket_solo, sport_ticket_duo, sport_ticket_famille

    def delete_cart(self):
        self.cart.clear()
        self.session.modified = True
