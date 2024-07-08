from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
    path('token/', views.TokenObtainAPIView.as_view(), name='token_obtain'),
    path('token/refresh/', views.TokenRefreshAPIView.as_view(), name='token_refresh'),
]

