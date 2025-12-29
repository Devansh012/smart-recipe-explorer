from django.db import models

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    cuisine = models.CharField(max_length=100)
    is_vegetarian = models.BooleanField(default=True)
    prep_time_minutes = models.IntegerField()
    ingredients = models.JSONField()
    difficulty = models.CharField(max_length=50)
    instructions = models.TextField()
    tags = models.JSONField()

    def __str__(self):
        return self.name