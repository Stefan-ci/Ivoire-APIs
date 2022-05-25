import random
from news.models import Article
from django.core.management.base import BaseCommand
from random_words import RandomWords, LoremIpsum, RandomNicknames


words = RandomWords()
lorem = LoremIpsum()
names = RandomNicknames()


authors = ['John DOE', 'Claver DIBY', 'Stefan CI', 'Kiuv ABRAJ']
langs = ['fr', 'en', 'de', 'ar', 'es', 'af', 'it', 'lat', 'por', 'ch', 'ru']
websites = ['www.stefanci.com', 'ivoire-hebdo.ci', 'ivoire-tv.net', 'opera.news']
dates = ['Lundi 4 Avril 2018', 'Mardi 16 Mai 2010', 'Jeudi 24 septembre 2022', 
    'Lundi 7 Septembre 1998']
picture_urls = ['www.stefanci.com/files/test.jpg', 'ivoire-hebdo.ci/files/hebdo.jpg',
    'ivoire-tv.net/files/vente_en_ligne.jpg', 'opera.news/files/safari.jpg']



class Command(BaseCommand):
    help = "Creates consecutively bunch of articles with a give number in the for loop"

    def handle(self, *args, **options):
        for i in range(1, 11):
    
            article = Article.objects.create(
                title=lorem.get_sentence(),
                author=random.choice(authors),
                picture_url=random.choice(picture_urls),
                content=lorem.get_sentences(15),
                summary=lorem.get_sentences(5),
                tags=lorem.get_sentence(),
                category=words.random_word(),
                published_on=random.choice(dates),
                language=random.choice(langs),
                website=random.choice(websites),
                # is_premium=False,
                # is_public=False,
                # is_submited=False,
            )

            ok = self.style.SUCCESS('OK')
            self.stdout.write(f">>>N°{i} created successfully: '{article}' .....{ok}\n\n")

            if not article:
                self.stderr.write(self.style.ERROR(f"Failed to create '{article}' !!!\n\n"))

        print('\n\n\n')
        print('======================================================================')
        print('======================================================================')
        print('======================================================================')
        
        print("\t\tArticles in db: %s" % Article.objects.all().count())
        print("\t\tPublic articles in db: %s" % Article.objects.filter(is_public=True).count())
        print("\t\tPrivate articles in db: %s" % Article.objects.filter(is_public=False).count())
        print("\t\tPremium articles in db: %s" % Article.objects.filter(is_premium=True).count())
        
        print('======================================================================')
        print('======================================================================')
        print('======================================================================')
        print('\n\n\n')



