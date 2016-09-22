from django.contrib import admin
from .models import BeerBrand, Vendor, Beer

# Register your models here.
admin.site.register(Beer)
admin.site.register(BeerBrand)
admin.site.register(Vendor)
