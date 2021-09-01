from django.db import models
import requests

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    @classmethod
    def add_categories(cls, name):
        cat = cls(name=name)
        #cat.save()
        print("cat saved !")


class Product(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    @classmethod
    def add_products(cls, name, url, nutriscore, categories):
        d = cls(name=name, url=url, nutriscore=nutriscore, categories=categories)
        d.save()
        print("data saved !")        

