from django.db import models


class Category(models.Model):
  name = models.CharField(max_length=500)
  description = models.TextField(blank=True, null=True)


class Menu(models.Model):
  name = models.CharField(max_length=500)
  description = models.TextField(blank=True, null=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=0, blank=True, null=True)
