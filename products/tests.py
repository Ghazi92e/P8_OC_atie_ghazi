from django.test.client import Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import response
from django.shortcuts import get_object_or_404
from products.models import Categories, Product, Product_favorite
from django.test import TestCase

class CategoriesTestCase(TestCase):
    def setUp(self):
        Categories.objects.create(name="pizza")
        User.objects.create(id=1)
        cat1 = get_object_or_404(Categories, name="pizza")
        Product.objects.create(id=5, name="lindt", url="http/test", nutriscore="e", image_product="http/image", nutrition_score_100g="2", categories=cat1)
        Product_favorite.objects.create(user_id=1, product_id=5)
    
    def test_add_categories(self):
        cat = Categories.objects.get(name="pizza")
        self.assertEqual(cat.add_categories(cat), cat)
    
    def test_add_products(self):
        cat1 = get_object_or_404(Categories, name="pizza")
        prod = Product.objects.get(name="lindt", image_product="http/image", url="http/test", nutriscore="e", nutrition_score_100g="2", categories=cat1)
        #self.assertEqual(prod.add_products(prod), prod)



class PublisherListViewTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.products_cat_url = reverse('products_cat')
        self.product_detail_url = reverse('product_detail', args=['1'])
        self.product_fav_url = reverse('fav_products')

        self.user = User.objects.create(id=1, username="test")
        Categories.objects.create(name="chocolate")
        cat1 = get_object_or_404(Categories, name="chocolate")
        self.product1 = Product.objects.create(
            name='lindt',
            url='http/product',
            nutriscore='e',
            image_product='htttp/image',
            nutrition_score_100g='1',
            categories=cat1
        )

    def test_get_products_by_cat(self):
        response = self.client.get(self.products_cat_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'purbeurre_project/home.html')
    
    def test_detail_prod(self):
        response = self.client.get(self.product_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
    
    def test_get_favorite_products(self):
        Product_favorite.objects.create(
            user_id=self.user.id,
            product_id=self.product1.id
        )
        response = self.client.post(self.product_fav_url, {
            'user_id': '1',
            'product_id':'2'
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.user.id, 1)
        self.assertEquals(self.product1.id, 2)
    

    

