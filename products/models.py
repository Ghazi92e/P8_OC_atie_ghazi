from django.db import models
from django.contrib.auth.models import User
import requests

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    @classmethod
    def add_categories(cls, name):
        cat = cls(name=name)
        cat.save()
        return name


class Product(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    image_product = models.CharField(max_length=200)
    nutrition_score_100g = models.CharField(max_length=10)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    @classmethod
    def add_products(cls, name, image_product, nutrition_score_100g, nutriscore, url, categories):
        data = cls(name=name, image_product=image_product, nutrition_score_100g=nutrition_score_100g, nutriscore=nutriscore, url=url, categories=categories)
        data.save()
        return data
class Product_favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    @classmethod
    def add_favorite_products(cls, user, product):
        favproducts = cls(user=user, product=product)
        favproducts.save()
        print("favproducts saved !")

