from rest_framework import routers
from .api import LeadViewSet,MobileUserViewSet
from django.urls import path

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