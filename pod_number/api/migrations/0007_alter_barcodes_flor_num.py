# Generated by Django 3.2.8 on 2021-10-18 07:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20211017_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barcodes',
            name='flor_num',
            field=models.ForeignKey(blank=True, max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.flornumber'),
        ),
    ]
