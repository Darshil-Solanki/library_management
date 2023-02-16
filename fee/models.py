from django.db import models
# Create your models here.
class Userdata(models.Model):
    profile_pic=models.ImageField(upload_to='images', blank=False)
    username = models.CharField(max_length=20) 
    fullname = models.CharField(max_length=35)
    no_book_issued = models.IntegerField()
    contact = models.IntegerField(unique=True)
    email = models.EmailField(max_length=30, unique=True) 
    db_table = "Userdata"