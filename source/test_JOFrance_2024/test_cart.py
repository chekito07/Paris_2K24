from django.test import TestCase, Client

from authentication.models import User
from cart.models import Solo
from cart.forms import DuoForm
from tickets.models import OffresTickets
from django.urls import reverse


class TestCartView(TestCase):
    def setUp(self):
        self.client = Client()
        self.data = {
            'holder_name': 'test_name',
            'card_number': 123456789,
            'card_validation_code': 456,
            'card_validity': '2022-11-01'
        }

    def test_get_cart_summary_view(self):
        url = reverse('cart_summary')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart_summary.html')

    def test_get_display_user_ticket_view(self):
        url = reverse('user-ticket')
        expected_url = '/login/?next=/cart/user_ticket/'
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'text/html; charset=utf-8')
        self.assertRedirects(response, expected_url)

    def test_credit_card_holder_info(self):
        url = reverse('card-holder')
        response = self.client.post(url, data=self.data, follow=True)
        expected_url = '/login/?next=/cart/card_holder/'
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, expected_url)


class TestOffresTicket(TestCase):
    def setUp(self):
        self.client = Client()
        self.solo = OffresTickets.objects.create(name='Ticket solo', price=35.00, number_of_place=1)
        self.duo = OffresTickets.objects.create(name='Ticket duo', price=65.00, number_of_place=2)
        self.famille = OffresTickets.objects.create(name='Ticket famille', price=130.00, number_of_place=4)
        self.products = self.client.session['session_key'] = {
            'ticket_solo': self.solo,
            'ticket_duo': self.duo,
            'ticket_famille': self.famille
        }

    def test_user_session_exist(self):
        self.assertTrue(self.client.session)

    def test_user_session_items(self):
        product = self.products
        self.assertEqual(product['ticket_famille'].price, 130.00)
        self.assertEqual(product['ticket_solo'].number_of_place, 1)


class TestModelSolo(TestCase):
    def setUp(self):
        self.data = {
            'username': 'test',
            'email': 'test@exemple.com',
            'password': 'test1234'
        }

        self.user = User.objects.create_user(**self.data)
        self.solo = Solo.objects.create(id='fd31bd88-a6c5-413a-84da-40e570e203dd', first_name='first', last_name='last',
                                        user=self.user)

    def test_if_solo_is_instance_of_model_solo(self):
        self.assertIsInstance(self.solo, Solo)

    def test_model_solo_field_label(self):
        ticket = Solo.objects.get(id='fd31bd88-a6c5-413a-84da-40e570e203dd')
        field_label = ticket._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'first name')

    def test_model_solo_max_length(self):
        ticket = Solo.objects.get(id='fd31bd88-a6c5-413a-84da-40e570e203dd')
        max_length = ticket._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 100)


class TestDuoForm(TestCase):
    def setUp(self):
        self.data = {
            'first_name': 'test_fname',
            'last_name': 'test_lname',
        }

    def test_if_form_is_instance_of_duoform(self):
        form = DuoForm()
        self.assertIsInstance(form, DuoForm)

    def test_duoform_placeholder(self):
        form = DuoForm()
        self.assertTrue(form.fields['first_name'].widget.attrs['placeholder'] == 'Prénom')

    def test_if_duoform_is_valid(self):
        form = DuoForm({'first_name': self.data['first_name'], 'last_name': self.data['last_name']})
        self.assertTrue(form.is_valid())















