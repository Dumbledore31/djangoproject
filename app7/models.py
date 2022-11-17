from django.db import models



# Create your models here.
class Table1(models.Model):
    Name=models.CharField(max_length=10)
    Age=models.IntegerField()
    Place=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)

class Gallery(models.Model):
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Name=models.CharField(max_length=10)
    Age=models.IntegerField()
    Place=models.CharField(max_length=10)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)
    