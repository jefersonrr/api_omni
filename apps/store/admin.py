from django.contrib import admin
from .models import Store,City,State,Country

# Register your models here.

admin.site.register(Store)
admin.site.register(City)
admin.site.register(State)
admin.site.register(Country)