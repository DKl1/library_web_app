from django.urls import path
from .views import *


urlpatterns = [
    path('orders/', orders_for_librarian, name='orders'),
    path('orders_user/', orders_for_user, name='orders_user'),
    path('close/<int:id>', close_order, name='close_order'),
    path('create/<int:book_id>', create_order, name='create_order'),
    path('order/edit/<int:id>/', update_order, name='update_order'),
]
