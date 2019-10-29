from rest_framework import serializers
from pages.models import Lead
from pages.models import MobileUser, ItemPurchase, OrderAmount
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

    validate_password = make_password


class ItemPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPurchase
        fields = '__all__'


class OrderAmountSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderAmount
        fields = '__all__'
