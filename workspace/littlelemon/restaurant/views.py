from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from django.http import HttpResponse
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view

# Create your views here.
# @api_view()
# @permission_classes([IsAuthenticated])
# def test(request):
#     return HttpResponse("Tessst")

# # Menu view
class MenuItemView (generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    
class SingleMenuItemView (generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# Booking view

class BookingViewSet (viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
