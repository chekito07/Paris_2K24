from django.test import TestCase, Client

from authentication.models import User

from authentication.forms import LoginForm, SignUpForm
from django.urls import reverse


# Create your tests here.
class TestUserModel(TestCase):
    def setUp(self):
        self.data = {
            'username': 'test',
            'email': 'test@exemple.com',
            'password': 'test1234'
        }

        self.user = User.objects.create_user(**self.data)

    def test_check_user_email(self):
        user = self.user
        self.assertEqual(user.email, 'test@exemple.com')

    def test_user_is_authenticated(self):
        user = self.user
        self.assertTrue(user.is_authenticated)

    def test_user_is_not_superuser(self):
        user = self.user
        self.assertFalse(user.is_superuser)


class TestAuthenticationForm(TestCase):
    def setUp(self):
        self.data = {
            'username': 'test',
            'first_name': 'test_fname',
            'last_name': 'test_lname',
            'email': 'test@exemple.com',
            'password1': 'test1234',
            'password2': 'test1234'
        }

    def test_form_is_instance_of_loginform(self):
        form = LoginForm()
        self.assertIsInstance(form, LoginForm)

    def test_loginform_is_valid(self):
        form = LoginForm({'username': self.data['username'], 'password': self.data['password1']})
        self.assertTrue(form.is_valid())

    def test_form_is_instance_of_signupform(self):
        form = SignUpForm()
        self.assertIsInstance(form, SignUpForm)


class TestAuthenticationView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_register_view(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')

    def test_post_register_view(self):
        data = {
            'username': 'test',
            'first_name': 'test_fname',
            'last_name': 'test_lname',
            'email': 'test@exemple.com',
            'password1': 'test1234',
            'password2': 'test1234'
        }

        url = reverse('register')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_get_login_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_login_view(self):
        data = {
            'username': 'test',
            'password': 'test1234',
        }

        url = reverse('login')
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
