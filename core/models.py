import jsonfield
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


SEX = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('undefined', 'Undefined')
)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(choices=SEX, default='undefined', max_length=10)
    api_key = models.CharField(max_length=200, unique=True, editable=False)
    hashed_api_key = models.CharField(max_length=200, unique=True, editable=False)
    extra_data = jsonfield.JSONField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date', 'age']



    def __str__(self):
        try:
            return str(self.user.email)
        except:
            return str(self.user.username)








class Documentation(models.Model):
    title = models.CharField(max_length=50)
    version = models.CharField(max_length=4, default='1.0')
    is_public = models.BooleanField(default=True, verbose_name="Public")
    summary = models.TextField(max_length=150)
    description = RichTextUploadingField()
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-date', 'is_public']
        verbose_name = "API Documentation"
        verbose_name_plural = "API Documentations"
    
    
    def __str__(self):
        return f"{self.title}, v.{self.version}"
