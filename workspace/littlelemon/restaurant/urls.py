from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
#You can rede README.md file for more details about API points
#There is an image folder that shows the results of the API code implementation

urlpatterns = [
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
    
]