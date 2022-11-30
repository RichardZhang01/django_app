from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.name} ({self.address})'


class Participant(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Meetup(models.Model):
    title = models.CharField(max_length=200)  # CharField is for shorter text
    # Specific for slugs. ALso generates an ID based on the slug which makes querying for the slug easier
    organizer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()  # TextField is for longer text
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE) # One-to-Many relationship
    participants = models.ManyToManyField(Participant, blank=True, null=True) # allows blank/nullable entries (not required)

    def __str__(self):
        return f'{self.title} - {self.slug}'
