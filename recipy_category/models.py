from django.db import models

# Create your models here.
class category_model(models.Model):
    category_name = models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)