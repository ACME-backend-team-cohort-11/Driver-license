from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DriverLicenseViewSet

router = DefaultRouter()
router.register(r'licenses', DriverLicenseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
