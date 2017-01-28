from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Carrier(models.Model):
    name = models.CharField(max_length=255)
    text_portal = models.CharField(max_length=255)

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    
class ReceipeItem(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=255, blank=True, null=True)
    
class Receipe(models.Model):
    ingredients = models.ManyToManyField(ReceipeItem, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    
class Roomate(models.Model):
    name = models.CharField(max_length=255)
    sys_user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    phone_carrier = models.ForeignKey(Carrier, null=True, blank=True)
    receipes = models.ManyToManyField(Receipe, null=True, blank=)
    monday_present = models.BooleanField()
    tuesday_present = models.BooleanField()
    wednesday_present = models.BooleanField()
    thursday_present = models.BooleanField()
    friday_present = models.BooleanField()
    saturday_present = models.BooleanField()
    sunday_present = models.BooleanField()

class Weekday(models.Model):
    date = models.DateField()
    cook = models.ForeignKey(Roomate)
    meal = models.ForeignKey(Receipe)
