from django.db import models

# Create your models here.
class Confession(models.Model):
	text = models.TextField(default="",null=False)
	ml_response = models.TextField(default="",null=False)