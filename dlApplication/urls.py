from django.urls import path
from .views import (
    CustomUserCreateView, CustomUserDetailView, CustomUserUpdateView,
    NewApplicationCreateView, NewApplicationDetailView, ApplicationUpdateView,
    RenewalCreateView, ReissueCreateView, TrackApplicationStatusView,
    RetrieveApplicationView, AcknowledgementSlipView
)

urlpatterns = [
    path('user/create/', CustomUserCreateView.as_view(), name='user-create'),
    path('user/<str:username>/', CustomUserDetailView.as_view(), name='user-detail'),
    path('user/<str:username>/update/', CustomUserUpdateView.as_view(), name='user-update'),
    path('application/create/', NewApplicationCreateView.as_view(), name='application-create'),
    path('application/<str:application_id>/', NewApplicationDetailView.as_view(), name='application-detail'),
    path('application/<str:application_id>/update/', ApplicationUpdateView.as_view(), name='application-update'),
    path('renewal/create/', RenewalCreateView.as_view(), name='renewal-create'),
    path('reissue/create/', ReissueCreateView.as_view(), name='reissue-create'),
    path('application/status/<str:application_id>/', TrackApplicationStatusView.as_view(), name='application-status'),
    path('application/retrieve/<str:identifier>/', RetrieveApplicationView.as_view(), name='application-retrieve'),
    path('application/acknowledgement/<str:application_id>/', AcknowledgementSlipView.as_view(), name='acknowledgement-slip'),
]
