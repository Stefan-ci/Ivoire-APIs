import random
from random_words import RandomWords
from receipes.models import Ingredient
from django.core.management.base import BaseCommand


words = RandomWords()
units = ['g', 'kg', 'l']




class Command(BaseCommand):
    help = "Creates consecutively bunch of ingredients with a give number in the for loop"

    def handle(self, *args, **options):
        for i in range(1, 1001):
            name = f'{words.random_word()} {words.random_word()}'
            quantity = f'{random.randint(1, 10)}{random.choice(units)}'
            ingredient = Ingredient.objects.create(
                name=name,
                quantity=quantity
            )
            
            
            ok = self.style.SUCCESS('OK')
            self.stdout.write(f">>>N°{i} created successfully: '{ingredient}' .....{ok}\n\n")

            if not ingredient:
                self.stderr.write(self.style.ERROR(f"Failed to create '{ingredient}' !!!\n\n"))

        print('\n\n\n')
        print('======================================================================')
        print('======================================================================')
        print('======================================================================')
        
        print("\tIngredients in db: %s" % Ingredient.objects.all().count())
        
        print('======================================================================')
        print('======================================================================')
        print('======================================================================')
        print('\n\n\n')



