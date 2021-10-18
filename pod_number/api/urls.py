from django.urls import path
from .import views


urlpatterns = [
    path('', views.navBar_dashboard, name="navbar"),
    path('create-buildingInfo/', views.post_buildingInfo, name="create-buildingInfo"),
    path('create-building/', views.testing, name="create-building"),
    path('addBuilding/', views.addBuilding, name="addBuilding"),
    path('postBarcodes/', views.postBarcodes, name="postBarcodes"),
    path('building-dropdown/', views.get_florNum, name="building-dropdown"),
       
]