from .models import Order, Product
from rest_framework import serializers
from django.contrib.auth.models import User

#Serializer class for Product 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product     
        fields = "__all__"

#Serializer class for order 
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

#Serializer class for user 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

