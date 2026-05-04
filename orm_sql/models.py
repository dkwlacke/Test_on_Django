from django.db import models

class User(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=128, null=True)
	surname = models.CharField(max_length=128, null=True)
	add_day = models.DateField(null=True)
	age = models.IntegerField(null=True)
	active = models.BooleanField(null=True)
	class_type = models.IntegerField(null=True)

	def __str__(self):
		return f'{self.id} | {self.name} | {self.surname} | {self.add_day} | {self.age} | {self.active} | {self.class_type}'
