import datetime

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from pages.models import FactOrders, PredictionOrder
from django.contrib.auth.hashers import make_password, check_password
from . import views
import time

# Create your views here.
from rest_framework.parsers import JSONParser

from pages.models import MobileUser
from pages.serializers import MobileUserSerializer


def index(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def today_data(request):
    orders_db = FactOrders.objects.using('mysql').all()
    order_count = 0
    sum_revenue = 0
    yesterday_revenue = 0

    # currently mocked
    today = '2017-03-03'
    yesterday = '2017-03-02'

    for order in orders_db:
        if order.order_purchase_timestamp[:10] == today:
            order_count += 1
            sum_revenue += order.price
        if order.order_purchase_timestamp[:10] == yesterday:
            # if order.order_purchase_timestamp[10:]<datetime.datetime.now().time():
            yesterday_revenue += order.price
    return JsonResponse({"order_count": order_count, "revenue": sum_revenue,
                         "comparision_yesterday": round((sum_revenue - yesterday_revenue) / sum_revenue, 2)})




def validate_user(request):
    req_json = json.loads(request.body)
    req_email = req_json['email']
    req_password = req_json['password']
    users = MobileUser.objects.all()

    for user in users:
        if user.email == req_email:
            print(make_password(req_password))
            print(req_json)
            serializer = MobileUserSerializer(data={'email': req_email, 'password': req_password})
            if serializer.is_valid():
                print("isvalid")
            else:
                print(serializer.error_messages)
            if MobileUserSerializer.validate_password(user.password, req_password):
                return JsonResponse({'message': 'Success'}, status=200)
            return JsonResponse({'message': 'Bad password'}, status=400)

    print(MobileUser.objects.all(), 'api/validate_user')
    return JsonResponse({'error': 'Bad Request'}, status=400)
