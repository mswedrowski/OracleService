import datetime
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json

from django.views.decorators.csrf import csrf_exempt

from pages.models import FactOrders, PredictionOrder
from django.contrib.auth.hashers import make_password, check_password
from . import views
from .tasks import sleepy
import time

# Create your views here.
from rest_framework.parsers import JSONParser

from pages.models import MobileUser
from pages.serializers import MobileUserSerializer


def index(request):
    return render(request, 'pages/index.html')

@csrf_exempt
def login(request):
    req_json = json.loads(request.body)
    req_username = req_json['username']
    req_password = req_json['password']

    users = MobileUser.objects.all()
    isOk = False
    for user in users:
        if(user.email==req_username and user.password==req_password):
            isOk = True
    if(isOk):
        return JsonResponse({'user': {'id': 5,'username':'test'},'token': '31111111111a'},status=200)
    else:
        return JsonResponse({'user': {'id': 5, 'username': 'wrong'}, 'token': '31111111111a'}, status=403)

def about(request):
    sleepy(10)
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
