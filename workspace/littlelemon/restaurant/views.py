from django.shortcuts import render
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework import generics,viewsets


# Create your views here.
# Menu view
class MenuItemView (generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    
class SingleMenuItemView (generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# Booking view
class BookingViewSet (viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
