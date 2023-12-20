from django.db import models
from django.contrib.auth.models import AbstractUser
sex =(
        ( 'female','F'),
        ('male','M')
    )

# Create your models here.
class User(AbstractUser):
    types=(
        ('tearcher','tearcher'),
        ('student','student'),
        ('secretary','secretary'),
        ('bursar','bursar'),
        ('dos','dos'),
        ('head','head')
           )
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=15)
    type =models.CharField(max_length=20, choices=types)
    image = models.ImageField(upload_to='pics',null=True)
class teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    department = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=sex)
    contact = models.CharField(max_length=15)
    email = models.CharField(max_length=20)
class student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    c_lass = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, choices=sex)
    parent_fname = models.CharField(max_length=30)
    parent_lname = models.CharField(max_length=30)
    parent_contact = models.CharField(max_length=30)
    parent_email = models.CharField(max_length=30)
    date_birth= models.DateField()
    adress =models.CharField(max_length=20)
class dos(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
class secretary(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
class bursar(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)
class management(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    contact = models.CharField(max_length=15)


