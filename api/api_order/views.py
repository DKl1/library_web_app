from rest_framework import generics
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated


class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Order.objects.filter(user_id=user_id)
