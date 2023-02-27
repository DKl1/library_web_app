from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('order', views.OrderView)
router.register(r'user/(?P<user_id>\d+)/order', views.OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls))
]