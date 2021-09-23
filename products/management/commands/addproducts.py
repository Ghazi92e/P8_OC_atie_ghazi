from products.models import Product, Categories
from django.core.management.base import BaseCommand
import requests


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.categories = [
            'pizza',
            'drink',
            'cheese',
            'chocolate',
        ]
        self.products = {}
        for cat in self.categories:
            r = requests.get(
                    'https://fr.openfoodfacts.org/cgi/search.pl',
                    params={
                        'json': 'true',
                        'search_terms': cat,
                        'search_tag': 'categories',
                        'fields': 'generic_name_fr,'
                        'nutrition_grades,url,image_url,fat_100g,'
                        'salt_100g,saturated-fat_100g,sugars_100g',
                        'tag_contains_0': 'contains',
                        'page_size': 30,
                        'page': 1,
                    },
                )
            res = r.json()
            self.products[cat] = res["products"]

        Command.filterdata(self)
        for cat in self.categories:
            r = Categories.objects.get(name=cat)
            for data in self.products[cat]:
                if len(data) > 7:
                    Product.add_products(data["fat_100g"],
                                         data["generic_name_fr"],
                                         data["image_url"],
                                         data["nutrition_grades"],
                                         data["salt_100g"],
                                         data["saturated-fat_100g"],
                                         data["sugars_100g"],
                                         data["url"], categories=r)
        print("Les produits ont été ajoutés à votre base de données !")

    def filterdata(self):
        for key in self.categories:
            for data in self.products[key]:
                try:
                    if data['generic_name_fr'] == '':
                        data.pop("generic_name_fr")
                    if data['nutrition_grades'] == '':
                        data.pop("nutrition_grades")
                    if data['url'] == '':
                        data.pop("url")
                except KeyError:
                    pass
