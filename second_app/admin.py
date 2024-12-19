from django.contrib import admin
from .models import Product,Purchase,Brand,Comment,Purchase
# Register your models here.
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Comment)
admin.site.register(Purchase)