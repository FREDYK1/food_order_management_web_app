from django.db import models
from django.contrib.auth.models import User

Meal_Types = (
        ("starters", "Starters"),
        ("salads", "Salads"),
        ("main_course", "Main Course"),
        ("desserts", "Desserts")
)

Status = (
        (0, "Unavailable"),
        (1, "Available")
)
class Order(models.Model):
    meal = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    price =models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(choices=Meal_Types, max_length=200)
    chef = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=Status, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
