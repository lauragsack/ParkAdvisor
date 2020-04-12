from django.db import models

from django.contrib.auth.models import User

# Create your models here.
CATEGORIES = (('L', 'Lodging'), ('A', 'Activities'), ('F', 'Food'))

class Park(models.Model):
	name = models.CharField(max_length=100)
	location = models.TextField(max_length=250)
	entrance_fee = models.IntegerField()
	description = models.TextField(max_length=250)
	phone = models.CharField(max_length=100)
	website = models.CharField(max_length=200)
	open = models.BooleanField()
	image = models.CharField(max_length=250)
	avg_rating = models.DecimalField(max_digits=2, decimal_places=1)

	def __str__(self):
		return self.name

class Review(models.Model):
	subject = models.CharField(max_length=100)
	created_date = models.DateField(auto_now_add=True)
	category = models.CharField(
		max_length=1,
		choices=CATEGORIES,
		default=CATEGORIES[1][1]
		)
	comments = models.TextField(max_length=250)
	image = models.CharField(max_length=250)
	park_rating = models.IntegerField()
	likes = models.IntegerField()

	#TODO ADD User foreign key a
	park = models.ForeignKey(Park, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.subject