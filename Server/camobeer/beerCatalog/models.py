from django.db import models

# Create your models here.
class BeerBrand(models.Model):
    brand_name = models.CharField(max_length=30)
    brand_logo = models.ImageField(upload_to="brands")

    def __str__(self):
        return self.brand_name

class Vendor(models.Model):
    vendor_name = models.CharField(max_length=30)
    vendor_logo = models.ImageField(upload_to="vendors")

    def __str__(self):
        return self.vendor_name

class Beer(models.Model):

    LATA = '1'
    LATAO = '2'
    GARRAFA = '3'
    LITRO = '4'
    GARRAFINHA = '5'

    BEER_SIZE = (
        (LATA, "Lata"),
        (LATAO, "Latao"),
        (LITRO, "Litro"),
        (GARRAFA, "Garrafa"),
        (GARRAFINHA, "Garrafinha"),
    )

    brand = models.ForeignKey(BeerBrand)
    beer_type = models.CharField(max_length=1, choices=BEER_SIZE)
    vendor = models.ForeignKey(Vendor)
    price = models.FloatField()

    def __str__(self):
        return ("%s %s %s" % (self.brand, self.get_beer_type_display(), self.vendor))

