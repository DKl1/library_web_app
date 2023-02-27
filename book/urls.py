from django.urls import path
from .views import *

urlpatterns = [
    path('', books, name='books'),
    path('book/<int:id>', about, name="about")
]
