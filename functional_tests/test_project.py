from selenium import webdriver
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.urls import reverse
from webdriver_manager.chrome import ChromeDriverManager
import time

from products.models import Categories, Product


class TestProjectListPage(StaticLiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        # self.browser = webdriver.Chrome('functional_tests/chromedriver')
        Categories.objects.create(name="pizza")
        data_cat = Categories.objects.get(name="pizza")
        Product.objects.create(name="mapizzadetest",
                               url="https", nutriscore="e",
                               image_product="httpsurl",
                               fat_100g=0.8, salt_100g=0.2,
                               saturated_fat_100g=0.1, sugars_100g=1.4,
                               categories=data_cat)

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
        time.sleep(5)

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
        time.sleep(5)

    def test_products_by_cat(self):
        self.browser.get(self.live_server_url)

        categories_input = self.browser.find_element_by_name("product_form")
        categories_input.send_keys("pizza")

        self.browser.find_element_by_xpath('//input'
                                           '[@value="recherche"]').click()

        time.sleep(5)

    def test_products_by_cat_error(self):
        self.browser.get(self.live_server_url)

        categories_input = self.browser.find_element_by_name("product_form")
        categories_input.send_keys("pizzaa")

        self.browser.find_element_by_xpath('//input'
                                           '[@value="recherche"]').click()

        data = self.browser
        self.assertEquals(
            data.find_element_by_tag_name('h1').text,
            'Erreur'
        )
        self.assertEquals(
            data.find_element_by_id('categories').text,
            "Veuillez saisir votre recherche avec les "
            "categories suivantes: pizza - drink - cheese ou chocolate"
        )

        time.sleep(5)
