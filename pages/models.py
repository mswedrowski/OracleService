# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# Create your models here.

class Lead(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class MobileUser(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class ItemPurchase(models.Model):
    itemName = models.CharField(max_length=100)
    date = models.FloatField(max_length=20)
    value = models.FloatField()


class OrderAmount(models.Model):
    date = models.FloatField(max_length=20)
    value = models.FloatField(default=0)



class CustomerCity(models.Model):
    customer_id = models.TextField(blank=True, null=True)
    customer_unique_id = models.TextField(blank=True, null=True)
    customer_zip_code_prefix = models.IntegerField(blank=True, null=True)
    customer_city = models.TextField(blank=True, null=True)
    customer_state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_city'


class FactOrders(models.Model):
    order_id = models.TextField(blank=True,primary_key=True)
    customer_id = models.TextField(blank=True, null=True)
    order_status = models.TextField(blank=True, null=True)
    order_purchase_timestamp = models.TextField(blank=True, null=True)
    order_approved_at = models.TextField(blank=True, null=True)
    order_delivered_carrier_date = models.TextField(blank=True, null=True)
    order_delivered_customer_date = models.TextField(blank=True, null=True)
    order_estimated_delivery_date = models.TextField(blank=True, null=True)
    order_item_id = models.IntegerField(blank=True, null=True)
    product_id = models.TextField(blank=True, null=True)
    seller_id = models.TextField(blank=True, null=True)
    shipping_limit_date = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    freight_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fact_orders'


class GeolocationCity(models.Model):
    geolocation_zip_code_prefix = models.IntegerField(blank=True, null=True)
    geolocation_lat = models.FloatField(blank=True, null=True)
    geolocation_lng = models.FloatField(blank=True, null=True)
    geolocation_city = models.TextField(blank=True, null=True)
    geolocation_state = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'geolocation_city'



class OrderItems(models.Model):
    order_id = models.TextField(blank=True, null=True)
    order_item_id = models.IntegerField(blank=True, null=True)
    product_id = models.TextField(blank=True, null=True)
    seller_id = models.TextField(blank=True, null=True)
    shipping_limit_date = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    freight_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_items'


class OrderPayments(models.Model):
    order_id = models.TextField(blank=True, null=True)
    payment_sequential = models.IntegerField(blank=True, null=True)
    payment_type = models.TextField(blank=True, null=True)
    payment_installments = models.IntegerField(blank=True, null=True)
    payment_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_payments'


class OrderReviews(models.Model):
    review_id = models.TextField(blank=True, null=True)
    order_id = models.TextField(blank=True, null=True)
    review_score = models.IntegerField(blank=True, null=True)
    review_comment_title = models.TextField(blank=True, null=True)
    review_comment_message = models.TextField(blank=True, null=True)
    review_creation_date = models.TextField(blank=True, null=True)
    review_answer_timestamp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_reviews'


class Products(models.Model):
    product_id = models.TextField(blank=True, null=True)
    product_category_name = models.TextField(blank=True, null=True)
    product_name_lenght = models.FloatField(blank=True, null=True)
    product_description_lenght = models.FloatField(blank=True, null=True)
    product_photos_qty = models.FloatField(blank=True, null=True)
    product_weight_g = models.FloatField(blank=True, null=True)
    product_length_cm = models.FloatField(blank=True, null=True)
    product_height_cm = models.FloatField(blank=True, null=True)
    product_width_cm = models.FloatField(blank=True, null=True)
    product_category_name_english = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'
