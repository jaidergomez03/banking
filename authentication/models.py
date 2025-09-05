from django.db import models

# Create your models here.
class User(models.Model):
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20,blank=True)
    #email= models.EmailField(max_length=150,unique=True)
    #password=models.TextField(max_length=128,unique=True)
    #mobile_number=models.CharField(max_length=15,unique=True)
    #address=models.CharField(max_length=255)
    #status=models.BooleanField(default=True)
    #created_at=models.DateTimeField(auto_now_add=True)
    #updated_at=models.DateTimeField(auto_now_add=True)
    #delete_at=models.DateTimeField(null=True)

class Department(models.Model):
    name= models.CharField(max_length=25)
    abrev=models.CharField(max_length=5)




