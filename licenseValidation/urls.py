from django.urls import path
from .views import ValidLicensesAPIView, ExpiredLicensesAPIView, FakeLicensesAPIView

urlpatterns = [
    path('licenses/valid/', ValidLicensesAPIView.as_view(), name='valid-licenses'),
    path('licenses/expired/', ExpiredLicensesAPIView.as_view(), name='expired-licenses'),
    path('licenses/fake/', FakeLicensesAPIView.as_view(), name='fake-licenses'),
]