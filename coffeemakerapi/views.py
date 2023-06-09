from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class CoffeemakerAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
