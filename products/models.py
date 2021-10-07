from django.db import models


class ProductManager(models.Manager):
    def name_sort(self):
        return self.order_by('-name')

    def category_sort(self):
        return self.order_by('-category')

    def rating_sort(self):
        return self.order_by('-rating')


class ProductDetails(models.Model):
    description = models.TextField()
    composition = models.TextField()
    contraindication = models.TextField()
    usage = models.TextField()
    elimination = models.TextField()


class Product(models.Model):
    objects = ProductManager()
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    imageUrl = models.URLField(max_length=200)
    rating = models.IntegerField(default=0)
    details = models.ForeignKey(
        ProductDetails, blank=True, null=True, on_delete=models.CASCADE)