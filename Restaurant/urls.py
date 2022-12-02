from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from core.views import index

from core.api.viewsets import ComandViewset, ItemViewset, WaiterViewset

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index')
]

