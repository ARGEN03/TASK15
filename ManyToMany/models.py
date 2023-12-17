from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=60)
    price = models.IntegerField()

    def __str__(self):
        return self.title

class Category(models.Model):
    CATEGORIES = [
        ('electronics', 'Электроника'),
        ('gadgets', 'Гаджеты'), 
        ('computers', 'Компьютеры'),
        ('clothes', 'Одежда'),
        ('shoes', 'Обувь'),
        ('household', 'Домашние товары')
    ]

    title = models.CharField(max_length=70, choices=CATEGORIES)
    products = models.ManyToManyField(Product, related_name='categories', related_query_name='category')

    def __str__(self):
        return self.title
