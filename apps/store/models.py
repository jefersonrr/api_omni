from django.db import models

# Create your models here.

class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False,blank=False)
    code = models.CharField(max_length=50, null=False,blank=False)
    def __str__(self):
        return self.name

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False,blank=False)
    code = models.CharField(max_length=50, null=False,blank=False)

    def __str__(self):
        return self.name

class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False,blank=False)
    code = models.CharField(max_length=50, null=False,blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, null=False,blank=False)
    code = models.CharField(max_length=50, null=False,blank=False)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    def __str__(self):
        return self.name