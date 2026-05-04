from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
	def create_user(self,username,first_name,last_name,password=None, **extra_fields):
		if not username:
			raise ValueError('The username field must be set')
		user = self.model(username=username,first_name=first_name,last_name=last_name,**extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self,username,first_name,last_name,password=None, **extra_fields):
		extra_fields.setdefault('is_staff',True)
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True')
		return self.create_user(username,first_name,last_name,password,**extra_fields)

class CustomUser(AbstractUser):
	#id = models.AutoField(primary_key=True)
	username = models.CharField(max_length=128,null=True, unique=True)
	first_name = models.CharField(max_length=128,null=True)
	last_name = models.CharField(max_length=128,null=True)

	objects = CustomUserManager()

	REQUIRED_FIELDS = ['first_name','last_name']

	def __str__(self):
		return self.username
