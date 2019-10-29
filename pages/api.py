from pages.models import Lead, MobileUser, OrderAmount, ItemPurchase
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer, MobileUserSerializer, OrderAmountSerializer, ItemPurchaseSerializer


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

    def validate_password(self, request):
        user = MobileUser.objects.all()
        serializer = MobileUserSerializer(data=request.data)
        if serializer.is_valid():
            user


class ItemPurchaseViewSet(viewsets.ModelViewSet):
    queryset = ItemPurchase.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ItemPurchaseSerializer


class OrderAmountViewSet(viewsets.ModelViewSet):
    queryset = OrderAmount.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrderAmountSerializer
