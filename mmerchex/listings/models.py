from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
...

        
class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        ARMB  = 'ARMB'
        
    class Type(models.TextChoices):
        disque = 'Record'
        vêtement ='Clothing'
        affiches = 'Posters' 
        divers = 'Miscellaneous'  
        
        
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices= Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    description = models.fields.CharField(max_length = 255, blank=True)
    sold = models.fields.IntegerField(max_length = 30)
    type = models.fields.CharField(choices = Type.choices, max_length = 100)
    images = models.ImageField( upload_to= "image")
    
    def __str__(self) -> str:
        return f'{self.name}'

class Prod(models.Model):
    title = models.fields.CharField(max_length = 100)
    prix = models.fields.IntegerField(max_length = 15)
    description = models.fields.TextField(max_length = 255) 
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    images = models.ImageField( upload_to= "image")
    
    def __str__(self) -> str:
        return f'{Prod.title}'