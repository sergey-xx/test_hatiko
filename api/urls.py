from django.urls import path, include
from .views import check_code

app_name = 'api_v1'

urlpatterns = [
    path("auth/", include("djoser.urls.jwt")),

    path('check-imei/', check_code, name='check_code'),
]
