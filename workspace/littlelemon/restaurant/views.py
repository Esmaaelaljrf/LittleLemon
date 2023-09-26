from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated



# Menu view
class MenuItemView (generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    
class SingleMenuItemView (generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# Booking view
class BookingViewSet (viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer