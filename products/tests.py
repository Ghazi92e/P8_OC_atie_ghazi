from products.views import PublisherListView
from products.forms import ProductForm
from django.test.client import Client, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from products.models import Categories, Product, Product_favorite
from django.test import TestCase
from http import HTTPStatus


class CategoriesTestCase(TestCase):
    def setUp(self):
        self.catname = "chocolate"

    def test_add_categories(self):
        cat = Categories(name="pizza")
        self.assertEquals(str(cat), cat.name)

    def test_add_cat_db(self):
        self.assertEquals(Categories.add_categories(self.catname), "chocolate")

    def test_add_products(self):
        products = Product(name="lindt")
        self.assertEquals(str(products), products.name)


class PublisherListViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.products_cat_url = reverse('products_cat')
        self.product_detail_url = reverse('product_detail', args=['1'])
        self.product_fav_url = reverse('fav_products')
        self.user = User.objects.create_user(username="test",
                                             email="test@gmail.com",
                                             password="testuser")

        self.user.save()
        self.client.login(username="test", password="testuser")
        Categories.objects.create(name="chocolate")
        cat1 = get_object_or_404(Categories, name="chocolate")
        self.product1 = Product.objects.create(
            name='lindt',
            url='http/product',
            nutriscore='e',
            image_product='htttp/image',
            fat_100g=1,
            salt_100g=2,
            saturated_fat_100g=3,
            sugars_100g=5,
            categories=cat1
        )

        Product_favorite.objects.create(user_id=self.user.id,
                                        product_id=self.product1.id)

    def test_get_products_by_cat(self):
        response = self.client.get(self.products_cat_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'purbeurre_project/home.html')

    def test_detail_prod(self):
        response = self.client.get(self.product_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_get_favorite_products(self):
        response = self.client.post(self.product_fav_url, {
            'user_id': self.user.id,
            'product_id': self.product1.id
        })
        self.assertEquals(response.status_code, 200)
        product_fav = Product_favorite.objects.all()
        self.assertEquals(product_fav.count(), 1)

    def test_get_favorite_products_url(self):
        response = self.client.get(self.product_fav_url)
        self.assertEquals(response.status_code, 200)

    def test_product_form_cat_url(self):
        form = self.client.post(self.products_cat_url,
                                data={"product_form": "pizza"})
        self.assertEquals(form.status_code, HTTPStatus.OK)

    def test_get_fav_product_login(self):
        self.resplog = self.client.get(self.product_fav_url)
        self.assertTrue(200, self.resplog.status_code)

    def test_product_form(self):
        form = ProductForm()
        self.assertTrue(form.fields['product_form'].label == ''
                        or form.fields['product_form'].label == 'Product form')

    def test_fav_prod_login_required(self):
        request = self.factory.get(self.product_fav_url)
        request.user = self.user
        response = PublisherListView.get_favorite_products((request))
        self.assertEqual(response.status_code, 200)
