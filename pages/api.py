from pages.models import Lead, MobileUser, OrderAmount, ItemPurchase, HistoryPurchase, TodayOrderDistribution, \
    TodayData,PredictionOrder
from rest_framework import viewsets, permissions
from .serializers import LeadSerializer, MobileUserSerializer, OrderAmountSerializer, ItemPurchaseSerializer, \
    HistoryPurchaseSerializer, TodayOrderDistributionSerializer, TodayOrderAmountSerializer,PredictionOrderSerializer


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


class HistoryPurchaseViewSet(viewsets.ModelViewSet):
    queryset = HistoryPurchase.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HistoryPurchaseSerializer


class TodayOrderDistributionViewSet(viewsets.ModelViewSet):
    queryset = TodayOrderDistribution.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodayOrderDistributionSerializer


class TodayOrderAmountViewSet(viewsets.ModelViewSet):
    queryset = TodayData.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TodayOrderAmountSerializer


class PredictionOrderViewSet(viewsets.ModelViewSet):
    queryset = PredictionOrder.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class =  PredictionOrderSerializer