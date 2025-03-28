"""
URL configuration for InventryManagementSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import Product_typeViewSet,ProductViewSet,DepartmentViewSet,SellViewSet,PurchaseViewSet,login, register, group_listing

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product-type/', Product_typeViewSet.as_view({'get':'list','post':'create'})),
    path('product-type/<int:pk>/', Product_typeViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('product/', ProductViewSet.as_view({'get':'list','post':'create'})),
    path('product/<int:pk>/', ProductViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('department/', DepartmentViewSet.as_view({'get':'list','post':'create'})),
    path('sell/', SellViewSet.as_view({'get':'list','post':'create'})),
    path('sell/<int:pk>/', SellViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('purchase/', PurchaseViewSet.as_view({'get':'list','post':'create'})),
    path('purchase/<int:pk>/', PurchaseViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('group/',group_listing),
    path('login/',login),
    path('register/',register),
]