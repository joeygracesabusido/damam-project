from django.urls import path
from .import views


urlpatterns = [
   
    path('create-buildingInfo/', views.post_buildingInfo, name="create-buildingInfo"),
       
]