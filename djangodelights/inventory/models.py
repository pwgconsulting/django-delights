from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)


class MenuItem(models.Model):
    title = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)


class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)

