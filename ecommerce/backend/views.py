from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated, SAFE_METHODS
from .models import Order, Product
from .serializers import ProductSerializer, OrderSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User

# Create your views here.
#Create ReadOnly class
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

# Product APIView That conducts get and post actions.
# Admin can add a product
# Other User can only see the product

class ProductAV(APIView):

    permission_classes = [IsAdminUser|ReadOnly]
    
    def get(self, request):
        DS = Product.objects.all()
        serializer = ProductSerializer(DS, many=True)
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


# Admin can Only update and delete a product
# Other User can only see the product details
class ProductDetailsAV(APIView):

    permission_classes = [IsAdminUser|ReadOnly]

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Customer User can search and view product
class ProductSearchAV(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, name):
        try:
            return Product.objects.get(name=name)
        except Product.DoesNotExist:
            raise Http404
    def get(self, request, name, format=None):
        snippet = self.get_object(name)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)


# User can place an order
class OrderAV(APIView):

    permission_classes = [IsAuthenticated]
    
        
    def post(self, request, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

# Admin can see the list of order
class OrderListAV(APIView):

    permission_classes = [IsAdminUser]
    def get(self, request):
        DS = Order.objects.all()
        serializer = OrderSerializer(DS, many=True)
        return Response(serializer.data)


# Admin can update delivery status
class OrderUpdateAV(APIView):
    permission_classes = [IsAdminUser]
    def get_object(self, pk):
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OrderSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = OrderSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#admin can see the list of user
class UserListAV(APIView):

    permission_classes = [IsAdminUser]
    
    def get(self, request):
        DS = User.objects.all()
        serializer = UserSerializer(DS, many=True)
        return Response(serializer.data)
        
   