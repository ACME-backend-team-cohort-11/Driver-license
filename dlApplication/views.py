from rest_framework import generics, permissions, status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import CustomUser, NewApplication, LicenseRenewal, LicenseReissue, ArchivedUser
from .serializers import CustomUserSerializer, NewApplicationSerializer, RenewalSerializer, ReissueSerializer, ArchivedUserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

class CustomUserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(username=response.data['username'])
        refresh = RefreshToken.for_user(user)
        response.data['refresh'] = str(refresh)
        response.data['access'] = str(refresh.access_token)
        return response

class CustomUserDetailView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated]

class CustomUserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'username'
    permission_classes = [permissions.IsAuthenticated]

class NewApplicationCreateView(generics.CreateAPIView):
    queryset = NewApplication.objects.all()
    serializer_class = NewApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class NewApplicationDetailView(generics.RetrieveAPIView):
    queryset = NewApplication.objects.all()
    serializer_class = NewApplicationSerializer
    lookup_field = 'application_id'
    permission_classes = [permissions.IsAuthenticated]

class RenewalCreateView(generics.CreateAPIView):
    queryset = LicenseRenewal.objects.all()
    serializer_class = RenewalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        application = get_object_or_404(NewApplication, user=self.request.user)
        archived_user = get_object_or_404(ArchivedUser, nin=self.request.user.nin)
        serializer.save(applicant=application, archived_user=archived_user)

class ReissueCreateView(generics.CreateAPIView):
    queryset = LicenseReissue.objects.all()
    serializer_class = ReissueSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        application = get_object_or_404(NewApplication, user=self.request.user)
        archived_user = get_object_or_404(ArchivedUser, nin=self.request.user.nin)
        serializer.save(applicant=application, archived_user=archived_user)

class TrackApplicationStatusView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, application_id, format=None):
        application = get_object_or_404(NewApplication, application_id=application_id, user=request.user)
        return Response({'status': application.status})

class ApplicationUpdateView(generics.UpdateAPIView):
    queryset = NewApplication.objects.all()
    serializer_class = NewApplicationSerializer
    lookup_field = 'application_id'
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveApplicationView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, identifier, format=None):
        try:
            if len(identifier) == 20:  # Assuming NIN has 20 characters
                application = get_object_or_404(NewApplication, nin=identifier)
            else:
                application = get_object_or_404(NewApplication, license_number=identifier)
            serializer = NewApplicationSerializer(application)
            return Response(serializer.data)
        except NewApplication.DoesNotExist:
            return Response({"detail": "Application not found."}, status=status.HTTP_404_NOT_FOUND)

class AcknowledgementSlipView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, application_id, format=None):
        application = get_object_or_404(NewApplication, application_id=application_id, user=request.user)
        nearest_location = application.center_location  # Assuming center_location has the nearest location info
        return Response({
            "application_id": application.application_id,
            "center_location": nearest_location,
            "message": "Please complete your biometrics at the mentioned location."
        })
