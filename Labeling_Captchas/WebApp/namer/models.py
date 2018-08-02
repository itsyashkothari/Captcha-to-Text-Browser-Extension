from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Image(models.Model):
	file_name = models.CharField(max_length = 100)
	value = models.CharField(max_length = 10)
	checked = models.BooleanField(default=False)
	solved_by = models.ForeignKey(User, on_delete=models.CASCADE ,null = True)
	def __str__(self):
		return self.file_name + '-' + self.value

class Profile(models.Model):
	user = models.OneToOneField(User, related_name = 'profile',on_delete=models.CASCADE)
	solved = models.IntegerField(blank = True,null = True,default = 0)

	
	