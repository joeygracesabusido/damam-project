from django.contrib import admin

# Register your models here.

from .models import Barcodes, florNumber

admin.site.register(Barcodes)
admin.site.register(florNumber)
