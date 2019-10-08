from rest_framework import serializers
from pages.models import Lead
from pages.models import MobileUser
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