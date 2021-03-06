from django import db
from django.db import models


# Create your models here.

class florNumber(models.Model):
    flor_number = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.id}-{self.flor_number}'

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

class Transactions(models.Model):
    """
    This is for Transaction model
    """ 
    flor_num = models.ForeignKey(florNumber, 
                                blank=True, null=True,
                                on_delete=models.CASCADE) 
    # flor_num = models.CharField(max_length=100 ,blank=True, null=True)
    barcode = models.CharField(max_length=100 ,blank=True, null=True)
    # type_sequence = models.CharField(max_length=100 ,blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.id}-{self.flor_num}'

    class Meta:
        
        db_table = 'transactions'


class TypeSequence(models.Model):
    """
    This is for Model TypeSequence
    
    """
    transaction = models.ForeignKey(Transactions, 
                                blank=True, null=True,
                                on_delete=models.CASCADE) 
    type_sequence = models.CharField(max_length=100 ,blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        
        db_table = 'TypeSequence'
        
    
    def __str__(self):
        return f'{self.id}-{self.type_sequence}'


class Transactionsdb(models.Model):

    """
    This is for database for 
    transaction with out the 
    tabular in line function
    """
    flor_num = models.ForeignKey(florNumber, 
                                blank=True, null=True,
                                on_delete=models.CASCADE) 
    # flor_num = models.CharField(max_length=100 ,blank=True, null=True)
    barcode = models.CharField(max_length=100 ,blank=True, null=True)
    type_sequence = models.CharField(max_length=100 ,blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        
        db_table = 'transactions_db'
        
    
    def __str__(self):
        return f'{self.id}-{self.type_sequence}'

