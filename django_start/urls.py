
from django.contrib import admin
from django.urls import path

from info.views import list_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', list_info)
]
