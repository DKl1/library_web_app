from django.urls import path, include
from . import views
from rest_framework import routers
from .views import SignUpView

router = routers.DefaultRouter()
router.register('user', views.CustomUserView)
router.register('users', views.UserDetailView)

urlpatterns = [
    path('', include(router.urls)),
    path('signup/', SignUpView.as_view(), name='signup'),

]
