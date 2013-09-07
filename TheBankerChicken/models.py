from django.db import models

class Account (models.Model):
	name = models.CharField(max_length = 100 , verbose_name = "Name")
	amount = models.IntegerField(max_length=10,verbose_name="amount")