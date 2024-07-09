from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('token/', views.TokenObtainAPIView.as_view(), name='token_obtain'),
    path('token/refresh/', views.TokenRefreshAPIView.as_view(), name='token_refresh'),
]

