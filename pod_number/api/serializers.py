from django.db import models
from django.db.models import fields
from rest_framework.relations import ManyRelatedField
from rest_framework.serializers import ModelSerializer
from .models import Barcodes
from rest_framework import serializers


class BarcodeSerialzers(ModelSerializer):
    class Meta:
        model = Barcodes
        fields ='__all__'