from rest_framework import routers
from .api import LeadViewSet, MobileUserViewSet, ItemPurchaseViewSet, OrderAmountViewSet, TodayOrderDistributionViewSet,\
    HistoryPurchaseViewSet,TodayOrderAmountViewSet,PredictionOrderViewSet
from django.urls import path
from pages.models import FactOrders, OrderAmount, Products, HistoryPurchase, TodayOrderDistribution,\
    TodayData,PredictionOrder
import time
import datetime
import threading

from . import views

router = routers.DefaultRouter()
router.register('api/leads', LeadViewSet, 'leads')
router.register('api/mobile_user', MobileUserViewSet, 'mobile_user')
router.register('api/purchase', ItemPurchaseViewSet, 'purchase')
router.register('api/order_amount', OrderAmountViewSet, 'order_amount')
router.register('api/history_purchase', HistoryPurchaseViewSet, 'history_purchase')
router.register('api/today_order_dist', TodayOrderDistributionViewSet, 'today_order_dist')
router.register('api/today_order', TodayOrderAmountViewSet, 'today_order')
router.register('api/prediction_order', PredictionOrderViewSet, 'prediction_order')

urlpatterns = router.urls

urlpatterns += [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('validate_user', views.validate_user, name='validate_user'),
    path('api/today_data', views.today_data, name='api/today_data'),
   # path('api/prediction_order', views.predict_orders, name='api/prediction_order')
]


def run():
    print('Starting server ...')

    orders_db = FactOrders.objects.using('mysql').all()
    products_db = Products.objects.using('mysql').all()

    start = datetime.datetime.now()

    productsList = []
    for products in products_db:
        productsList.append(products.product_category_name_english)
    products = set(productsList)

    purchaseDataList = []
    for order in orders_db:
        purchaseDataList.append(order.order_purchase_timestamp[:10])

    purchaseDates = set(purchaseDataList[:10])

    order_amount_id = 0

    today = purchaseDataList[0]  # just mocking right now because i've got past data
    # today = datetime.date.today()
    yesterday = '2017-03-03'

    for date in purchaseDates:
        count = purchaseDataList.count(date)
        if count is None:
            count = 0

        timestamp = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())
        if count > 0:
            OrderAmount(order_amount_id, timestamp, count).save()
        order_amount_id += 1

        dictOfProducts = {i: 0 for i in products}

        for order in orders_db:
            if order.order_purchase_timestamp[:10] == date:
                try:
                    product_related = products_db.get(product_id=order.product_id)
                    for key, value in dictOfProducts.items():
                        if key == product_related.product_category_name_english:
                            dictOfProducts[key] = value + 1

                except Products.DoesNotExist:
                    pass

        if date == today:
            sum_today = 0
            rev_value = 0
            for k, v in dictOfProducts.items():
                sum_today += v
            for k, v in dictOfProducts.items():
                if k != '':
                    TodayOrderDistribution(itemName=k, distribution=(v / sum_today)).save()
            for order in orders_db:
                if order.order_purchase_timestamp[:10] == date:
                    rev_value += order.price

        timestamp = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())
        for k, v in dictOfProducts.items():
            if k != '':
                HistoryPurchase(itemName=k, date=timestamp, value=float(v)).save()

    print(datetime.datetime.now() - start)



def predict_orders():
    PredictionOrder.objects.all().delete()
    today = '2017-03-03'
    next_day = '2017-03-04'
    next_day_2 = '2017-03-05'
    next_day_3 = '2017-03-06'
    list_of_dates = (next_day, next_day_2, next_day_3)

    val = 55

    for date in list_of_dates:
        timestamp = time.mktime(datetime.datetime.strptime(date, "%Y-%m-%d").timetuple())
        PredictionOrder(date=timestamp, value=val).save()
        val += 1

predict_orders()


def clear_all():
    OrderAmount.objects.all().delete()
    HistoryPurchase.objects.all().delete()
    TodayOrderDistribution.objects.all().delete()
    TodayData.objects.all().delete()
    PredictionOrder.objects.all().delete()




print("START!")
run()
predict_orders()
print('sth')
