from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class book(models.Model):
    name=models.CharField(max_length=100, blank=False)
    isbn=models.CharField(max_length=14, blank=False)
    authors=ArrayField(models.CharField(max_length=100, blank=False))
    number_of_pages=models.IntegerField()
    publisher=models.CharField(max_length=100, blank=False)
    country=models.CharField(max_length=25, blank=False)
    release_date=models.DateField()