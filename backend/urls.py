from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('api.urls')),
    path('admin/', admin.site.urls),
    path('liveconfigs/', include('liveconfigs.urls'), name='liveconfigs'),
]
