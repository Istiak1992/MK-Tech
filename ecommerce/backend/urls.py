from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    path('product/', ProductAV.as_view(), name="Product"),
    path('productDetails/<int:pk>/', ProductDetailsAV.as_view(), name="productDetails"),
    path('ProductSearch/<str:name>/', ProductSearchAV.as_view(), name="ProductSearch"),

    path('order/', OrderAV.as_view(), name="order"),
    path('getorder/', OrderListAV.as_view(), name="getorder"),
    
    path('orderupdate/<int:pk>/', OrderUpdateAV.as_view(), name="orderupdate"),
    path('userlist/', UserListAV.as_view(), name="userlist"),

    
    
   
    

]

urlpatterns = format_suffix_patterns(urlpatterns)

