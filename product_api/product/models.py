from django.db import models

# Create your models here.
class product_info(models.Model):
	title = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	image = models.FileField()
	description = models.CharField(max_length=500)
	category = models.CharField(max_length=10)