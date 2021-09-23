from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls.base import reverse


class LoginTest(TestCase):
    def setUp(self):
        self.c = Client()
        self.account = {
            'username': 'test',
            'email': 'test@gmail.com',
            'password': 'testok'
        }
        User.objects.create_user(**self.account)
        self.username = 'test1'
        self.email = 'test1@gmail.com'
        self.password = 'testok'

    def test_user_register(self):
        res = self.c.get(reverse('register'))
        self.assertEquals(res.status_code, 200)

    def test_login(self):
        res = self.c.get('/users/login/')
        self.assertEquals(res.status_code, 200)

    def test_login_user(self):
        data = self.c.post('/users/login/', self.account)
        res = self.c.login(username='test',
                           email='test@gmail.com', password='testok')
        self.assertEquals(data.status_code, 302)
        self.assertEquals(res, True)

    def test_user_account(self):
        res = self.c.get('/users/account')
        self.assertEquals(res.status_code, 200)

    def test_logout_user(self):
        res = self.c.get('/users/login/deconnexion/')
        self.assertEquals(res.status_code, 302)

    def test_user_register_form(self):
        res = self.c.post(reverse('register'), data={
            'username': self.username,
            'email': self.email,
            'password': self.password
        })
        self.assertEquals(res.status_code, 302)
        users = User.objects.all()
        self.assertEquals(users.count(), 2)

    def test_user_register_template(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
