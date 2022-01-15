from django.db import models
category_choice=(('Vegetable','Vegetable'),
                 ('Fruit','Fruit'),
                 ('Nuts','Nuts'))
# Create your models here.
class FoodItem(models.Model):
    Name = models.CharField(max_length=1000)
    Type = models.CharField(max_length=2000,choices=category_choice)
    Vitamin_Present= models.CharField(max_length=1000)
