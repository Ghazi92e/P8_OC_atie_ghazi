from products.models import Categories
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        categories = [
            'pizza',
            'drink',
            'cheese',
            'chocolate',
        ]
        for cat in categories:
            Categories.add_categories(cat)
        print("Les catégories ont été ajoutées à votre base de données !")
