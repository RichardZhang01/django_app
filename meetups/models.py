from django.db import models

# Create your models here.

class Meetup(models.Model):
    title = models.CharField(max_length=200) # CharField is for shorter text
    slug = models.SlugField(unique=True) # Specific for slugs. ALso generates an ID based on the slug which makes querying for the slug easier
    description = models.TextField() # TextField is for longer text
    image = models.ImageField(upload_to='images')
