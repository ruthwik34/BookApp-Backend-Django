from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(blank=True, max_length=120)
    description = models.TextField(blank=True, null=True)
    release_date = models.DateField(blank=True)
    read_counter = models.IntegerField(blank=True)
