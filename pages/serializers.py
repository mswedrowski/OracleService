from rest_framework import serializers
from pages.models import Lead
from pages.models import MobileUser, ItemPurchase, OrderAmount, HistoryPurchase, TodayOrderDistribution, \
    TodayData, PredictionOrder
from django.contrib.auth.hashers import make_password


# Lead Serialzier
class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'


class MobileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileUser
        fields = '__all__'

   # validate_password = make_password


class ItemPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPurchase
        fields = '__all__'


class OrderAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAmount
        fields = '__all__'


class HistoryPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryPurchase
        fields = '__all__'


class TodayOrderDistributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayOrderDistribution
        fields = '__all__'


class TodayOrderAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodayData
        fields = '__all__'


class PredictionOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionOrder
        fields = '__all__'
