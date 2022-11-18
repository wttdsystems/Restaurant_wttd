from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from core.api.viewsets import ComandViewset, ItemViewset, WaiterViewset

routers = routers.DefaultRouter()

routers.register(r'comand/', ComandViewset, basename='comand')
routers.register(r'item/', ItemViewset, basename='item')
routers.register(r'waiter/', WaiterViewset, basename='waiter')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(routers.urls)),
]

