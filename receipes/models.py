from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField








class Cuisine(models.Model):
    name = models.CharField(null=True, blank=True, max_length=20, unique=True)
    other_details = models.TextField(null=True, blank=True)
    added_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-added_on', 'name']


    def __str__(self):
        return str(self.name)











class Ingredient(models.Model):
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








"""Below are proxy models. Used for filtering receipes and display them like tables"""
class PremiumReceipe(Receipe):
    class Meta:
        proxy = True
        verbose_name = "Premium Receipe"
        verbose_name_plural = "Premium Receipes"




class NonPremiumReceipe(Receipe):
    class Meta:
        proxy = True
        verbose_name = "Non-premium Receipe"
        verbose_name_plural = "Non-premium Receipes"
    



class PrivateReceipe(Receipe):
    class Meta:
        proxy = True
        verbose_name = "Private Receipe"
        verbose_name_plural = "Private Receipes"




class PublicReceipe(Receipe):
    class Meta:
        proxy = True
        verbose_name = "Public Receipe"
        verbose_name_plural = "Public Receipes"




class SubmitedReceipe(Receipe):
    class Meta:
        proxy = True
        verbose_name = "Submited Receipe"
        verbose_name_plural = "Submited Receipes"



class NonSubmitedReceipe(Receipe):
    class Meta:
        proxy = True
        verbose_name = "Non-submited Receipe"
        verbose_name_plural = "Non-submited Receipes"






