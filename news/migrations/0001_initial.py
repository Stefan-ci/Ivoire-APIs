# Generated by Django 3.2.9 on 2022-05-23 19:02

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='No title', max_length=500, null=True)),
                ('author', models.CharField(blank=True, default='No author', max_length=500, null=True)),
                ('picture_url', models.CharField(blank=True, default='No picture', max_length=500, null=True)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='No content', null=True)),
                ('summary', models.TextField(blank=True, default='No summary', null=True)),
                ('tags', models.TextField(blank=True, default='No tags', null=True)),
                ('category', models.CharField(blank=True, default='No category', max_length=200, null=True)),
                ('published_on', models.CharField(blank=True, default='No date found', max_length=200, null=True)),
                ('language', models.CharField(blank=True, default='Not defined', max_length=50, null=True)),
                ('website', models.CharField(blank=True, default='Not provided', max_length=100, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('is_premium', models.BooleanField(default=False)),
                ('is_submited', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('submited_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-added_on', 'title', 'language', 'category'],
            },
        ),
    ]
