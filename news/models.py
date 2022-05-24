import string
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    submited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(null=True, blank=True, max_length=500, default='No title')
    author = models.CharField(null=True, blank=True, max_length=500, default='No author')
    picture_url = models.CharField(null=True, blank=True, max_length=500, default='No picture')
    content = RichTextUploadingField(null=True, blank=True, default='No content')
    summary = models.TextField(null=True, blank=True, default='No summary')
    tags = models.TextField(null=True, blank=True, default='No tags')
    category = models.CharField(null=True, blank=True, max_length=200, default='No category')
    published_on = models.CharField(null=True, blank=True, max_length=200, default='No date found')
    language = models.CharField(null=True, blank=True, max_length=50, default='Not defined')
    website = models.CharField(null=True, blank=True, max_length=100, default='Not provided')
    
    is_public = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)
    is_submited = models.BooleanField(default=False)

    added_on = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ['-added_on', 'title', 'language', 'category']
    
    

    def __str__(self):
        return str(self.title)



    """Methods to handle easily with each article."""
    def article_tags(self):
        """
            Since tags are saved as sentence, make sure it's the default one 
            then return a list of words that sentence while removing ponctuations and apostrophes.
        """
        if self.tags == 'No tags':
            return 'No tags'
        words = self.tags

        exclude = set(string.punctuation)
        return ''.join(word for word in words if word not in exclude).split()







"""Below are proxy models. Used for filtering articles and display them like tables"""
class PremiumArticle(Article):
    class Meta:
        proxy = True
        verbose_name = "Premium article"
        verbose_name_plural = "Premium articles"




class NonPremiumArticle(Article):
    class Meta:
        proxy = True
        verbose_name = "Non-premium article"
        verbose_name_plural = "Non-premium articles"
    



class PrivateArticle(Article):
    class Meta:
        proxy = True
        verbose_name = "Private article"
        verbose_name_plural = "Private articles"




class PublicArticle(Article):
    class Meta:
        proxy = True
        verbose_name = "Public article"
        verbose_name_plural = "Public articles"




class SubmitedArticle(Article):
    class Meta:
        proxy = True
        verbose_name = "Submited article"
        verbose_name_plural = "Submited articles"



class NonSubmitedArticle(Article):
    class Meta:
        proxy = True
        verbose_name = "Non-submited article"
        verbose_name_plural = "Non-submited articles"

