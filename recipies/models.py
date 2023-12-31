from django.db import models
from django.contrib.auth.models import User
# Create your models here.
meals=[
    ('Dessert','Dessert'),
    ('Main Course','Main Course'),
    ('Appetizer','Appetizer'),
    
]
class recipyModel(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    ingredients=models.TextField()
    instructions=models.TextField()
    image=models.ImageField(upload_to='recipy/',blank=True)
    category=models.CharField(max_length=50,choices=meals)
    
    def __str__(self):
        return self.title
    