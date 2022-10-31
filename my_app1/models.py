from datetime import date
from email.headerregistry import Address
from statistics import mode
from django.db import models
from django.forms import CharField

# Create your models here.
class Producto(models.Model):
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.type} | {self.name} | {self.brand}"

class Cliente(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=40)
    phone_namber = models.IntegerField()
    email = models.CharField(max_length=35)
    company = models.CharField(max_length=35)
    
    def __str__(self):
        return f"{self.name} | {self.last_name} | {self.address}| {self.phone_namber}| {self.email}| {self.company}"
    
class Empleado(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date = models.DateField()
    address = models.CharField(max_length=40)
    phone_namber = models.IntegerField()
    email = models.CharField(max_length=35)
    
    def __str__(self):
        return f"{self.name} | {self.last_name} | {self.date}| {self.address}| {self.phone_namber}| {self.email}"