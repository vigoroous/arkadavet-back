from django.db import models


class ProductManager(models.Manager):
    def name_sort(self):
        return self.order_by('-name')

    def category_sort(self):
        return self.order_by('-category')

    def rating_sort(self):
        return self.order_by('-rating')


class Category(models.Model):
    id = models.CharField(max_length=60, primary_key=True)
    name = models.CharField(max_length=200)


class Details(models.Model):
    description = models.TextField()
    composition = models.TextField()
    contraindication = models.TextField()
    usage = models.TextField()
    elimination = models.TextField()


class Product(models.Model):
    objects = ProductManager()
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, blank=True, null=True, on_delete=models.CASCADE)
    imageUrl = models.URLField(max_length=200)
    rating = models.IntegerField(default=0)
    details = models.ForeignKey(
        Details, blank=True, null=True, on_delete=models.CASCADE)