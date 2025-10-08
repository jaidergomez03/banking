from django.db import models
    
class Country(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} {self.abrev}" 

class Department(models.Model):
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5)
    id_country = models.ForeignKey(Country, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True) 
    
    def __str__(self):
        return f"{self.name} {self.abrev}" 
    
class City(models.Model):
    id_department = models.ForeignKey(Department, on_delete=models.CASCADE, default=1) 
    name = models.CharField(max_length=20)
    abrev = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} {self.abrev}" 

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=13, null=True, blank=True) 
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=45)
    password = models.TextField()
    id_city = models.ForeignKey(City, on_delete=models.CASCADE, default=1)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True) 
    
    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.mobile_phone} {self.address} {self.email} {self.password} {self.id_city} {'Activate' if self.status else 'Inactive'}"










