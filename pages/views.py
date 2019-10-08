from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.contrib.auth.hashers import make_password, check_password
import django.contrib.auth.password_validation


# Create your views here.
from rest_framework.parsers import JSONParser

from pages.models import MobileUser
from pages.serializers import MobileUserSerializer


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')

def validate_user(request):
    req_json = json.loads(request.body)
    req_email = req_json['email']
    req_password = req_json['password']
    users = MobileUser.objects.all()

    for user in users:
        if user.email == req_email:
            print(make_password(req_password))
            print(req_json)
            serializer = MobileUserSerializer(data= {'email': req_email, 'password': req_password})
            if serializer.is_valid():
                print("isvalid")
            else:
                print(serializer.error_messages)
            if MobileUserSerializer.validate_password(user.password, req_password):
                return JsonResponse({'message': 'Success'}, status=200)
            return JsonResponse({'message': 'Bad password'}, status=400)

    print(MobileUser.objects.all(),'api/validate_user')
    return JsonResponse({'error':'Bad Request'},status=400)