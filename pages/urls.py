from rest_framework import routers
from .api import LeadViewSet,MobileUserViewSet
from django.urls import path
from pages.models import FactOrders,OrderAmount
import time
import datetime

from . import views

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet,'leads')
router.register('api/mobile_user', MobileUserViewSet,'mobile_user')

urlpatterns = router.urls


urlpatterns += [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('validate_user',views.validate_user,name='validate_user')
]

def run():
    orders_db = FactOrders.objects.using('mysql').all()

    purchaseDataList = []

    for order in orders_db:
        purchaseDataList.append(order.order_purchase_timestamp[:10])

    purchaseDates = set(purchaseDataList)


    for date in purchaseDates:
        print(date)
        print(purchaseDataList.count(date))
        print(time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple()))

        count = purchaseDataList.count(date)
        if (count is None):
            count = 0

        timestamp = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())

        print(timestamp)
        print(count)

        OrderAmount(timestamp, count).save()
        print()


run()