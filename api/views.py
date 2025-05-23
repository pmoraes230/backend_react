from django.shortcuts import render
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

# Create your views here.
class ItemListCreate(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer