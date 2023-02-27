from django.urls import path
from .views import *


urlpatterns = [
    path('authors/', author_page, name='authors'),
    path('authors/<int:id>', delete_author, name='delete_authors'),
    path('authors/create', create_author, name='create_author'),
    path('author/edit/<int:id>', update_author, name='update_author')
]