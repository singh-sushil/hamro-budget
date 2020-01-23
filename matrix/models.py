from django.db import models

# Create your models here.
class signup(models.Model):
    name = models.CharField(max_length=20)
    citizenship_no = models.CharField(max_length = 20)
    photo = models.ImageField(upload_to = '')
    citizenship_scan = models.FileField(upload_to = '')
    username = models.CharField(max_length=10)
    password1 = models.CharField(max_length = 10)
    password2 = models.CharField(max_length = 10)





