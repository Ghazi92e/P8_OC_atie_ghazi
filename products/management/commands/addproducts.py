from products.models import Categories, Product
from django.core.management.base import BaseCommand, CommandError
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
                        'fields': 'generic_name_fr,code,'
                                    'nutrition_grades,url,stores',
                        'tag_contains_0': 'contains',
                        'page_size': 30,
                        'page': 1,
                    },
                )
            res = r.json()
            self.products[cat] = res["products"]
        Command.filterdata(self)
        #print(self.products)
        #Categories.add_categories(cat)
        
        for cat in self.categories:
            r = Categories.objects.get(name=cat)
            for data in self.products[cat]:
                if len(data) > 4:
                    Product.add_products(data["generic_name_fr"], data["url"], data["nutrition_grades"], categories=r)

    def filterdata(self):
        for key in self.categories:
            for data in self.products[key]:
                try:
                    if data['generic_name_fr'] == '':
                        data.pop("generic_name_fr")
                    if data['code'] == '':
                        data.pop("code")
                    if data['nutrition_grades'] == '':
                        data.pop("nutrition_grades")
                    if data['url'] == '':
                        data.pop("url")
                    if data['stores'] == '':
                        data.pop("stores")
                except KeyError:
                    pass
