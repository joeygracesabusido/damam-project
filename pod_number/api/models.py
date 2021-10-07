from django import db
from django.db import models

# Create your models here.

class Barcodes(models.Model):
    flor_num = models.CharField(max_length=100)
    barcode = models.CharField(max_length=100)

    def __str__(self):
        return self.flor_num

    class Meta:
        ordering = ['flor_num']
        db_table = 'barcodes'

        
