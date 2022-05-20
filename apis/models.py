from django.db import models

# Create your models here.


class Country(models.Model):
	data_type = models.CharField(max_length=10)
	main_location = models.CharField(max_length=50)
	capital = models.CharField(max_length=50)

	def __str__(self):
		return str(self.main_location)


class State(models.Model):
	data_type = models.CharField(max_length=10)
	main_location = models.CharField(max_length=50)
	capital = models.CharField(max_length=50)

	def __str__(self):
		return str(self.main_location)


class City(models.Model):
	data_type = models.CharField(max_length=10)
	main_location = models.CharField(max_length=50)
	capital = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return str(self.main_location)

 
class Language(models.Model):
	name = models.CharField(max_length=40)

	def __str__(self):
		return str(self.name)


class Population(models.Model):
	country = models.ForeignKey(Country, on_delete=models.PROTECT, null=True, blank=True, related_name="country")
	city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True, related_name="city")
	state = models.ForeignKey(State, on_delete=models.PROTECT, null=True, blank=True, related_name="state")
	language = models.ForeignKey(Language, on_delete=models.PROTECT, null=True, blank=True, related_name='language')
	population = models.CharField(max_length=40)

	def __str__(self):
		 return str(self.id)
