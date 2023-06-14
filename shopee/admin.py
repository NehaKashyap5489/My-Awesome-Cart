from django.contrib import admin
from .models import product,contact,Order,OrderUpdate

# Register your models here.
admin.site.register(product)
admin.site.register(contact)
admin.site.register(Order)
admin.site.register(OrderUpdate)

