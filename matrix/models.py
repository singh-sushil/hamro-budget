from django.db import models

# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=20)
    citizenship_no = models.CharField(max_length = 20)
    photo = models.ImageField(upload_to = '')
    citizenship_scan = models.FileField(upload_to = '')
    username = models.CharField(max_length=10)
    password = models.CharField(max_length = 10)
    confirm_password = models.CharField(max_length = 10)

class local_bodies_id(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length = 20)





