from rest_framework import serializers
from .models import Vendor, BeerBrand, Beer

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        field = ('vendor_name')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerBrand
        field = ('brand_name')

class BeerSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    vendor = VendorSerializer()

    class Meta:
        model = Beer
        field = ('brand', 'beer_type', 'vendor')

