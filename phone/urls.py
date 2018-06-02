from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from . import views

router = DefaultRouter()
router.register(r'call-start-records', views.CallStartRecordViewSet)
router.register(r'call-end-records', views.CallEndRecordViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
