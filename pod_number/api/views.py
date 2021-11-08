from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Barcodes, florNumber

from rest_framework.decorators import api_view

from .serializers import BarcodeSerialzers
from rest_framework.response import Response


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages, auth


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
        # print(request.POST)
        flor_number_id = request.POST.get('floor_categories')
        barcode2 = request.POST.get('Barcode')
        flor_number = florNumber.objects.get(id=flor_number_id)

       
        # for flor_alert in Barcodes.objects.all():

        # flor_alert = Barcodes.objects.all()
        # for e in Barcodes.objects.all():
        if Barcodes.objects.filter(barcode = barcode2):
        
            return HttpResponse('Record already exist')
        
        else:

            db_save = Barcodes.objects.create(
                flor_num = flor_number,

                barcode = barcode2
            )

            return redirect('barcode-list')


    else:
        return render(request,"navbar.html",{})

def get_florNum(request):
    results = florNumber.objects.all()
    # context = {"flor_number": flor_number}
    return render(request, "insertBarcode.html", {"showflor": results})

def get_florNum2(request):
    results = florNumber.objects.all()
    return render(request, "barcodelist.html", {"showflor": results})

def barcodeList(request):
    """
    This function is for 
    barcode list 
    """

    if request.method=="POST":
        
        search_param = request.POST.get('flornum')
       
        searchResult = Barcodes.objects.raw('SELECT id, flor_num_id, barcode \
                                            from Barcodes where \
                                            barcode like "%'+ search_param +'%"')
       
        return render (request,"barcodelist.html", {"blist": searchResult})
        
    else:
        searchResult = Barcodes.objects.all()
        return render(request, "barcodelist.html", {"blist": searchResult})


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

# this is for login function
def loginPage(request):
    #return render(request, 'accounts/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect('navbar')
        else:
            messages.error(request, "Invalid username or password.")
    else:
        messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request,
                  "login.html",
                  {"form": form})


def logout_user(request):
    logout(request)
    messages.success(request,("You were Logged Out!!!"))
    return redirect('login')


def get_Barcode(request):
    results = Barcodes.objects.all()
    # context = {"flor_number": flor_number}
    return render(request, "transactions.html", {"showBarcode": results})


def transaction_post(request):
    """
    This is for posting Transaction
    """

    if request.method=="POST":
        
        search_param = request.POST.get('barcode')
       
        searchResult2 = Barcodes.objects.raw('SELECT id, flor_num_id, barcode \
                                            from Barcodes where \
                                            barcode like "%'+ search_param +'%"')
       
        return render (request,"transaction.html", {"blist": searchResult2})
        
    else:
        searchResult2 = Barcodes.objects.all()
        return render(request, "transaction.html", {"blist": searchResult2})




