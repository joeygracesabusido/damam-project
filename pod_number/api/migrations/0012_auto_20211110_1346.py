# Generated by Django 3.2.8 on 2021-11-10 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_transactions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactions',
            name='barcode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='flor_num',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='type_sequence',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
