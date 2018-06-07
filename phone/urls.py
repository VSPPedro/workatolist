from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from django.urls import path
from . import views

router = DefaultRouter()
router.register(r'call-start-records', views.CallStartRecordViewSet)
router.register(r'call-end-records', views.CallEndRecordViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    path('<phone_number>/', views.last_bill, name='last_bill'),
    path('<phone_number>/<int:year>/<int:month>/', views.bill, name='bill'),
]
