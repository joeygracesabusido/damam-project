from django import db
from django.db import models


# Create your models here.

class florNumber(models.Model):
    flor_number = models.CharField(max_length=100)

    def __str__(self):
        return self.flor_number

    class Meta:
        
        db_table = 'florNumber'

   

class Barcodes(models.Model):
    flor_num = models.ForeignKey(florNumber, max_length=100,
                                blank=True, null=True, on_delete=models.CASCADE)
    barcode = models.CharField(max_length=100)
    
    update = models.DateTimeField(auto_now=True)
    # created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['flor_num']
        db_table = 'barcodes'

        
