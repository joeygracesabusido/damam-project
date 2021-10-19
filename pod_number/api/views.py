from django.shortcuts import redirect, render
from .models import Barcodes, florNumber

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

# this is for Nav bar

def navBar_dashboard(request):
    return render(request, 'navbar.html')

def testing(request):
    return render(request, 'add.html')


def addBuilding(request):
    """
    This function is for adding 
    flor number
    """

    if request.method == 'POST':

        flor_number = request.POST.get('flor_number')
        
        db_save = florNumber.objects.create(
            flor_number=flor_number
        )
        
        return render(request, 'navbar.html')

def insert_dasBoard(request):
    return render(request, 'insertBarcode.html')


def postBarcodes(request):
    """
    This function is for posting
    barcodes
    """
    if request.method == 'POST':
        
        flor_number_id = request.POST.get('floor_categories')
        barcode = request.POST.get('Barcode')
        flor_number = florNumber.objects.get(id=flor_number_id)



        db_save = Barcodes.objects.create(
            flor_num = flor_number,
            barcode = barcode
        )

        return redirect('barcode-list')


    else:
        return render(request,"navbar.html",{})

def get_florNum(request):
    results = florNumber.objects.all()
    # context = {"flor_number": flor_number}
    return render(request, "insertBarcode.html", {"showflor": results})

def barcodeList(request):
    """
    This function is for 
    barcode list 
    """
    results = Barcodes.objects.all()
    return render(request, "barcodelist.html", {"blist": results})

def barcodelist2(request):
    return render(request, 'barcodelist.html')

def deleteBarcode(request,id):
    """
    This function is for
    Deleting Entry for Barcode
    """
    barcodes = Barcodes.objects.get(pk=id)
    barcodes.delete()
    return redirect('barcode-list')
