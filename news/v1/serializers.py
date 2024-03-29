from news.models import Article
from rest_framework.serializers import ModelSerializer, ReadOnlyField



class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['title', 'author', 'picture_url', 'content', 'summary', 
            'article_tags', 'category', 'published_on', 'language', 'website', 'full_url']



