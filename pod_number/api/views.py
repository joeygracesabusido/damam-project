from django.shortcuts import render
from .models import Barcodes

from rest_framework.decorators import api_view

from .serializers import BarcodeSerialzers
from rest_framework.response import Response

@api_view(['POST'])
def post_buildingInfo(request):
    """
    This function is for creating or to add 
    building infro API
    """
    data = request.data
    addbuildingInfo= Barcodes.objects.create(
        flor_num=data['flor_num'],
        barcode=data['barcode']
        
    )
    serializer = BarcodeSerialzers(addbuildingInfo, many=False)
    return Response(serializer.data)


