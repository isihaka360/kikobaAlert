from django.contrib import admin
from .models import Customer

# Here is where we register our Customer model in Admin site.
admin.site.register(Customer)
