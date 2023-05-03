"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from django.views.generic import TemplateView

from CustomToken import CustomTokenObtainPairView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('book.urls')),
    path('', include('order.urls')),
    path('', include('author.urls')),
    path('api/v1/', include('api.api_authentication.urls')),
    path('api/v1/', include('api.api_author.urls')),
    path('api/v1/', include('api.api_order.urls')),
    path('api/v1/', include('api.api_book.urls')),
    path('api/v1/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    # path('api-auth/', include("rest_framework.urls")),
    # path('api/rest-auth/', include("rest_auth.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
# urlpatterns += [re_path(r'^(?P<path>.*)$', serve, {'document_root': settings.REACT_APP_DIR})]
