from pages.models import Lead, MobileUser
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer,MobileUserSerializer

# Lead viewset
class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LeadSerializer

class MobileUserViewSet(viewsets.ModelViewSet):
    queryset = MobileUser.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MobileUserSerializer

    def validate_password(self,request):
        user = MobileUser.objects.all()
        serializer = MobileUserSerializer(data=request.data)
        if serializer.is_valid():
            user