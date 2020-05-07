from djongo import models
# from django.db import models
from django.urls import reverse


# Create your models here.
class Producttype(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.category


class Product(models.Model):
    producttype = models.ForeignKey(Producttype, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=1000, null=True)
    summary = models.TextField(null=True, blank=True)
    featured = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f"/product/{self.id}/"
        return reverse("products:product_details", kwargs={"id":self.id})
