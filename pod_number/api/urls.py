from django.urls import path
from .import views


urlpatterns = [
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('', views.navBar_dashboard, name="navbar"),
    path('create-buildingInfo/', views.post_buildingInfo, name="create-buildingInfo"),
    path('create-building/', views.testing, name="create-building"),
    path('addBuilding/', views.addBuilding, name="addBuilding"),
    path('postBarcodes/', views.postBarcodes, name="postBarcodes"),
    path('building-dropdown/', views.get_florNum, name="building-dropdown"),
    path('building-dropdown-list/', views.get_florNum2, name="building-dropdown-list"),
    path('barcode-list/', views.get_transaction, name="barcode-list"), 
    path('barcode-list2/', views.barcodeList, name="barcode-list2"), 
    path('barcode-delete/<int:id>/', views.deleteBarcode, name="barcode-delete"),
    path('search_barcode/', views.get_Barcode, name="search_barcode"),
    path('test/', views.testing_ajax, name="test"),
    path('insert-transactons/', views.transaction_post, name="insert-transactons"),
    path('search_barcode/transactions-list/', views.get_transaction, name="search_barcode/transactions-list"), 
    path('transactions-delete/<int:id>/', views.deleteTransaction, name="transactions-delete"),
]