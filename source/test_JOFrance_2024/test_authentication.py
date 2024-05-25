from django.test import TestCase, Client

from authentication.models import User

from authentication.forms import LoginForm, SignUpForm
from django.urls import reverse


# Create your tests here.
class TestRegisterView(TestCase):
    def setUp(self):
        self.data = {
            'username': 'test',
            'first_name': 'test_fname',
            'last_name': 'test_lname',
            'email': 'test@exemple.com',
            'password1': 'test1234',
            'password2': 'test1234'
        }

        self.client = Client()

    def test_get_register_view(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')

    def test_post_register_view(self):
        url = reverse('register')
        response = self.client.post(url, data=self.data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/register.html')


class TestLoginView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', email='test@exemple.com', password='test1234')

    def test_get_login_view(self):
        url = reverse('login')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(type(response.content), bytes)

    def test_post_login_view(self):
        url = reverse('login')
        response = self.client.post(url, username='test', password='test1234')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/login.html')
        self.assertEqual(response.request.get('username'), 'test')
        self.assertEqual(response.request.get('password'), 'test1234')

    def test_check_user_email(self):
        user = self.user
        self.assertEqual(user.email, 'test@exemple.com')

    def test_user_is_authenticated(self):
        user = self.user
        self.assertTrue(user.is_authenticated)


class TestLoginForm(TestCase):
    def setUp(self):
        self.data = {
            'username': 'test',
            'password': 'test1234'
        }

    def test_if_form_is_instance_of_loginform(self):
        form = LoginForm()
        self.assertIsInstance(form, LoginForm)

    def test_if_loginform_is_valid(self):
        form = LoginForm({'username': self.data['username'], 'password': self.data['password']})
        self.assertTrue(form.is_valid)
        self.assertEqual(form.data['password'], 'test1234')


class TestSignUpForm(TestCase):
    def setUp(self):
        self.data = {
            'username': 'test',
            'first_name': 'test_fname',
            'last_name': 'test_lname',
            'email': 'test@exemple.com',
            'password1': 'test1234',
            'password2': 'test1234'
        }

    def test_if_form_is_instance_of_signupform(self):
        form = SignUpForm()
        self.assertIsInstance(form, SignUpForm)

    def test_if_signupform_is_valid(self):
        form = SignUpForm(data={'username': self.data['username'], 'first_name': self.data['first_name'], 'last_name': self.data['last_name'],
                           'email': self.data['email'], 'password1': self.data['password1'], 'password2': self.data['password2']})
        self.assertTrue(form.is_valid)
        self.assertEqual(form.data['password1'], 'test1234')
