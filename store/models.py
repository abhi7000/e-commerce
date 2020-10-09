from django.db import models
from datetime import date

# Create your models here.
class Product(models.Model):
	product_id=models.AutoField
	product_name=models.CharField(max_length=50,default="")
	desc=models.CharField(max_length=300,default="")
	pub_date=models.DateField(default=date.today)
	sub_cat=models.CharField(max_length=50,default="")
	image=models.ImageField(upload_to='store/images',default=" ")
	price=models.IntegerField(default=0)

	def __str__(self):
		return self.product_name

class Contact(models.Model):
	user_id=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50,default="")
	desc=models.CharField(max_length=300,default="")
	email=models.CharField(max_length=300,default="")
	phone=models.CharField(max_length=50,default="")

	def __str__(self):
		return self.name