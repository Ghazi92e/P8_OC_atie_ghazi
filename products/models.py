from django.db import models
from django.contrib.auth.models import User
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
    fat_100g = models.DecimalField(max_digits=5, decimal_places=2)
    salt_100g = models.DecimalField(max_digits=5, decimal_places=2)
    saturated_fat_100g = models.DecimalField(max_digits=5, decimal_places=2)
    sugars_100g = models.DecimalField(max_digits=5, decimal_places=2)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    @classmethod
    def add_products(cls, fat_100g, name, image_product, nutriscore,
                     salt_100g, saturated_fat_100g, sugars_100g,
                     url, categories):
        data = cls(fat_100g=fat_100g, name=name, image_product=image_product,
                   nutriscore=nutriscore, salt_100g=salt_100g,
                   saturated_fat_100g=saturated_fat_100g,
                   sugars_100g=sugars_100g, url=url, categories=categories)
        data.save()


class Product_favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    @classmethod
    def add_favorite_products(cls, user, product):
        favproducts = cls(user=user, product=product)
        favproducts.save()
