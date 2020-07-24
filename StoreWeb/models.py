from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title




class Product(models.Model):
    name = models.CharField('Nombre', max_length=100)
    description = models.TextField('Descripcion', max_length=255)
    quantity = models.IntegerField('Cantidad')


class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField('Nombre', max_length=100)
    value = models.DecimalField('Valor', max_digits=12, decimal_places=2)


class Taxes(models.Model):
    product = models.ManyToManyField(Product)
    name = models.CharField('Nombre', max_length=100)
    value = models.DecimalField('Valor', max_digits=12, decimal_places=2)
