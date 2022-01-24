from django.contrib import admin

# Register your models here.
from api import models

from .models import Barcodes, florNumber, Transactions,Transactionsdb

admin.site.register(Barcodes)
admin.site.register(florNumber)
admin.site.register(Transactionsdb)
# admin.site.register(Transactions)


class TypeSequenceInline(admin.TabularInline):
    model = models.TypeSequence

@admin.register(models.Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    inlines = [TypeSequenceInline]