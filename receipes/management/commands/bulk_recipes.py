import random
from random_words import RandomWords, LoremIpsum
from django.core.management.base import BaseCommand
from receipes.models import Ingredient, Receipe, Cuisine


words = RandomWords()
lorem = LoremIpsum()

cuisines  = Cuisine.objects.all()
ingredients  = Ingredient.objects.all()


class Command(BaseCommand):
    help = "Creates consecutively bunch of recipes with a give number in the for loop"

    def handle(self, *args, **options):
        for i in range(1, 1001):
            
            cuisine = random.choice(list(cuisines))    
            ings = random.sample(list(ingredients), 10)
    
            recipe = Receipe.objects.create(
                name=lorem.get_sentence(),
                details=lorem.get_sentences(5),
                tags=lorem.get_sentence(),
                category=words.random_word(),
                cuisine=cuisine,
                #is_premium=True,
                #is_public=False,
                #is_submited=True,
            )
            
            recipe.ingredients.set(ings)

            ok = self.style.SUCCESS('OK')
            self.stdout.write(f">>>N°{i} created successfully: '{recipe}' .....{ok}\n\n")

            if not recipe:
                self.stderr.write(self.style.ERROR(f"Failed to create '{recipe}' !!!\n\n"))

        print('\n\n\n')
        print('======================================================================')
        print('======================================================================')
        print('======================================================================')
        
        print("\t\trecipes in db: %s" % Receipe.objects.all().count())
        print("\t\tPublic recipes in db: %s" % Receipe.objects.filter(is_public=True).count())
        print("\t\tPrivate recipes in db: %s" % Receipe.objects.filter(is_public=False).count())
        print("\t\tPremium recipes in db: %s" % Receipe.objects.filter(is_premium=True).count())
        
        print('======================================================================')
        print('======================================================================')
        print('======================================================================')
        print('\n\n\n')



