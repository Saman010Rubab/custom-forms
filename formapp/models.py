from django.db import models

class Product(models.Model):
    name = models.CharField( max_length=100)
    quantity = models.IntegerField()
    image=models.ImageField( upload_to='products/images')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

