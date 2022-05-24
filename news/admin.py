from news.models import Article
from django.contrib import admin
from news.utils import ArticleModelAdminStuffs
from news.models import PremiumArticle, NonPremiumArticle, PrivateArticle
from news.models import PublicArticle, SubmitedArticle, NonSubmitedArticle





class ArticleAdmin(ArticleModelAdminStuffs):
    list_display = ['title', 'author', 'added_on']
    list_filter = ['is_public', 'is_premium', 'is_submited', 'added_on', 'language']
    





"""Below are proxy models admin customizations"""

class PremiumAdmin(ArticleModelAdminStuffs):
    list_display = ['title', 'author', 'is_premium', 'added_on']
    list_filter = ['is_public', 'is_submited', 'added_on', 'language']


    def get_queryset(self):
        qs = super().get_queryset()
        qs = Article.objects.filter(is_premium=True)
        return qs








class NonPremiumAdmin(ArticleModelAdminStuffs):
    list_display = ['title', 'author', 'is_premium', 'added_on']
    list_filter = ['is_public', 'is_submited', 'added_on', 'language']


    def get_queryset(self):
        qs = super().get_queryset()
        qs = Article.objects.filter(is_premium=False)
        return qs







class PrivateAdmin(ArticleModelAdminStuffs):
    list_display = ['title', 'author', 'is_public', 'added_on']
    list_filter = ['is_premium', 'is_submited', 'added_on', 'language']


    def get_queryset(self):
        qs = super().get_queryset()
        qs = Article.objects.filter(is_public=False)
        return qs







class PublicAdmin(ArticleModelAdminStuffs):
    list_display = ['title', 'author', 'is_public', 'added_on']
    list_filter = ['is_premium', 'is_submited', 'added_on', 'language']


    def get_queryset(self):
        qs = super().get_queryset()
        qs = Article.objects.filter(is_public=True)
        return qs








class SubmitedAdmin(ArticleModelAdminStuffs):
    list_display = ['title', 'author', 'is_submited', 'added_on']
    list_filter = ['is_public', 'is_premium', 'added_on', 'language']


    def get_queryset(self):
        qs = super().get_queryset()
        qs = Article.objects.filter(is_submited=True)
        return qs








class NonSubmitedAdmin(ArticleModelAdminStuffs):
    list_display = ['title', 'author', 'is_submited', 'added_on']
    list_filter = ['is_public', 'is_premium', 'added_on', 'language']


    def get_queryset(self):
        qs = super().get_queryset()
        qs = Article.objects.filter(is_submited=False)
        return qs







admin.site.register(Article, ArticleAdmin)

admin.site.register(PremiumArticle, PremiumAdmin)
admin.site.register(NonPremiumArticle, NonPremiumAdmin)

admin.site.register(PrivateArticle, PrivateAdmin)
admin.site.register(PublicArticle, PublicAdmin)

admin.site.register(SubmitedArticle, SubmitedAdmin)
admin.site.register(NonSubmitedArticle, NonSubmitedAdmin)

