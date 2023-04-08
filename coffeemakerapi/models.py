from django.db import models

class CategoryProduct(models.Model):
    name = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=200, null=True)
    average_consumption = models.DecimalField(max_digits=30, decimal_places=18, null=True)

    def __str__(self):
        return self.name