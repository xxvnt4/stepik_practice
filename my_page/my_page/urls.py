from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('horoscope/', include('horoscope.urls')),
    path('week_days/', include('week_days.urls')),
    path('geometry/', include('geometry.urls')),
    path('reeves/', include('reeves.urls'))
]
