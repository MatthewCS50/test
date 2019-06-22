from django.db import models

# Create your models here.
SIZES = (
	("S", "Small"),
	("L", "Large")
)

STYLES = (
	("R", "Regular"),
	("S", "Silican")
)

TYPES = (
	("S", "Special"),
	("N", "Normal")
)



class Topping(models.Model):
	name = models.CharField(max_length=32)

	def __str__(self):
		return f"{self.name}"

class Pizza(models.Model):
	style = models.CharField(max_length=1, choices=STYLES)
	size = models.CharField(max_length=1, choices=SIZES)
	number_toppings = models.IntegerField()#models.ManyToManyField(Topping, blank=True)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	base = models.CharField(max_length=1, choices=TYPES, blank=True)

	def __str__(self):
		return f"{self.get_base_display()} {self.get_size_display()} {self.get_style_display()} Pizza with {self.number_toppings} Topping(s) - ${self.price}"

class Addition(models.Model):
	name = models.CharField(max_length=32)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.name} - ${self.price}"

	atomic=False

class Sub(models.Model):
	size = models.CharField(max_length=1, choices=SIZES)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	name = models.CharField(max_length=32)
	additions = models.ManyToManyField(Addition, blank=True)

	def __str__(self):
		return f"{self.get_size_display()} {self.name} - ${self.price}"

class Pasta(models.Model):
	name = models.CharField(max_length=32)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.name} - ${self.price}"

class Salad(models.Model):
	name = models.CharField(max_length=32)
	price = models.DecimalField(max_digits=5, decimal_places=2)

	def __str__(self):
		return f"{self.name} - {self.price}"

class DinnerPlatter(models.Model):
	size = models.CharField(max_length=1, choices=SIZES)
	price = models.DecimalField(max_digits=5, decimal_places=2)
	name = models.CharField(max_length=32)

	def __str__(self):
		return f"{self.get_size_display()} {self.name} - ${self.price}"