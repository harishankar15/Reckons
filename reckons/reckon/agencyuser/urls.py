from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('addstock', views.addstock,name='addstock'),
    path('addbill', views.addbill,name='addbill'),
    path('adduser', views.adduser,name='adduser'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('addoutlet',views.addoutlet,name='addoutlet'),
   
]