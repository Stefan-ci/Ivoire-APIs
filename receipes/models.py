import string
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField








class Cuisine(models.Model):
    submited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=20)
    other_details = models.TextField(null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-added_on', 'name']


    def __str__(self):
        return str(self.name)











class Ingredient(models.Model):
    submited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=500)
    quantity = models.CharField(null=True, blank=True, max_length=20)
    added_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-added_on', 'name', 'quantity']


    def __str__(self):
        return f"{self.quantity} of {self.name}"











class Receipe(models.Model):
    submited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(null=True, blank=True, max_length=500, default='No name')
    category = models.CharField(null=True, blank=True, max_length=200, default='No category')
    tags = models.TextField(null=True, blank=True, default='No tags')
    details = RichTextUploadingField(null=True, blank=True, default='No details')
    ingredients = models.ManyToManyField(Ingredient)
    cuisine = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True, blank=True)

    is_public = models.BooleanField(default=True)
    is_premium = models.BooleanField(default=False)
    is_submited = models.BooleanField(default=False)

    added_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-added_on', 'name', 'category']


    def __str__(self):
        return str(self.name)



    """Methods to handle easily with each article."""
    def receipe_tags(self):
        """
            Since tags are saved as sentence, make sure it's the default one 
            then return a list of words that sentence while removing ponctuations 
            and apostrophes.
        """
        if self.tags == 'No tags':
            return 'No tags'
        words = self.tags

        exclude = set(string.punctuation)
        return ''.join(word for word in words if word not in exclude).split()



