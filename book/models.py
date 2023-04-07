from django.conf import settings
from django.db import models


class Book(models.Model):
    class LanguageType(models.TextChoices):
        UZBEK = 'uzbek', 'Uzbek'
        ENGLISH = 'english', 'English'
        RUSSIAN = 'russian', 'Russian'

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.FloatField()
    sale_percent = models.PositiveSmallIntegerField(default=0)
    best_seller = models.BooleanField(default=False)
    pub_year = models.PositiveIntegerField(null=True)
    page_size = models.PositiveIntegerField()
    lang = models.CharField(max_length=50, choices=LanguageType.choices)
    file = models.FileField()
    image = models.ImageField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name="book")
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name="book")


class Category(models.Model):
    name = models.CharField(max_length=100)


class Author(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

# class BookLanguage(models.Model):
#     language = models.CharField(max_length=50)
