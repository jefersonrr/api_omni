from django.db import models
from apps.store.models import City,Country,Store,State

# Create your models here.

class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name =models.CharField(max_length=200, null=False,blank=False)
    surname = models.CharField(max_length=200, null=False,blank=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    favorite_store = models.ForeignKey(Store, on_delete=models.CASCADE)
    def __str__(self):
        return self.surname