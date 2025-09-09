from django.db import models


class Users(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    password = models.TextField()
    mobile_number = models.CharField(max_length=15, unique=True)
    address = models.CharField(max_length=255)
    id_city = models.ForeignKey("Cities", on_delete=models.SET_NULL, null=True, blank=True, related_name="users")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Countries(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Departments(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=5)
    id_country = models.ForeignKey("Countries", on_delete=models.CASCADE, null=True, blank=True, related_name="departments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)


class Cities(models.Model):
    name = models.CharField(max_length=50)
    abrev = models.CharField(max_length=5)
    id_department = models.ForeignKey("Departments", on_delete=models.CASCADE, null=True, blank=True, related_name="cities")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)














