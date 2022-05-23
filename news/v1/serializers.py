from news.models import Article
from rest_framework.serializers import ModelSerializer, ReadOnlyField



class ArticleSerializer(ModelSerializer):
    submited_by = ReadOnlyField(source='submited_by.username')
    class Meta:
        model = Article
        fields = ['id', 'submited_by', 'title', 'author', 'picture_url', 'content', 'summary', 
            'article_tags', 'category', 'published_on', 'language', 'website', 'is_premium', 
            'is_public', 'is_submited', 'added_on']



