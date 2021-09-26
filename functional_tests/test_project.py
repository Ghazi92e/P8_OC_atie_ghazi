from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
import time


class TestProjectListPage(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('functional_tests/chromedriver')

    def tearDown(self):
        self.browser.close()

    def test_home_project(self):
        self.browser.get(self.live_server_url)

        data = self.browser.find_element_by_class_name('masthead')
        self.assertEquals(
            data.find_element_by_tag_name('h1').text,
            'Du gras, oui, mais de qualité !'
        )

    def test_user_create_account(self):
        url = reverse("register")
        self.browser.get(self.live_server_url + url)

        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys('test')

        email_input = self.browser.find_element_by_name("email")
        email_input.send_keys('test@gmail.com')

        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('test11')

        self.browser.find_element_by_xpath('//input[@value="Créer un compte"]'
                                           ).click()
        time.sleep(10)

    def test_user_login(self):
        url = '/users/login/'
        self.browser.get(self.live_server_url + url)

        username_input = self.browser.find_element_by_name("username")
        username_input.send_keys('test')

        email_input = self.browser.find_element_by_name("email")
        email_input.send_keys('test@gmail.com')

        password_input = self.browser.find_element_by_name("password")
        password_input.send_keys('test11')

        self.browser.find_element_by_xpath('//input[@value="Se connecter"]'
                                           ).click()
        time.sleep(10)
