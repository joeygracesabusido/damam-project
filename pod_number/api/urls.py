from django.urls import path
from .import views


urlpatterns = [
    path('', views.loginPage, name="login"),
    path('navbar/logout/', views.logout_user, name="logout"),
    path('navbar/', views.navBar_dashboard, name="navbar"),
    path('navbar/create-buildingInfo/', views.post_buildingInfo, name="create-buildingInfo"),
    path('navbar/create-building/', views.testing, name="create-building"),
    path('addBuilding/', views.addBuilding, name="addBuilding"),
    path('postBarcodes/', views.postBarcodes, name="postBarcodes"),
    path('navbar/building-dropdown/', views.get_florNum, name="building-dropdown"),
    path('navbar/building-dropdown-list/', views.get_florNum2, name="building-dropdown-list"),
    path('navbar/barcode-list/', views.barcodeList, name="barcode-list"), 
    path('barcode-list2/', views.barcodelist2, name="barcode-list2"), 
    path('barcode-delete/<int:id>/', views.deleteBarcode, name="barcode-delete"),
]