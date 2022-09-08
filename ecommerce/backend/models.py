from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    image1 = models.CharField(max_length=300, null=True, blank=True)
    image2 = models.CharField(max_length=300, null=True, blank=True)


    def __str__(self):
        return self.name


class Order(models.Model):
    orderId = models.CharField(max_length=300, null=True, blank=True)
    orderBy = models.CharField(max_length=300, null=True, blank=True)
    productList = models.CharField(max_length=300, null=True, blank=True)
    total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    deliveryStatus = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.orderId
