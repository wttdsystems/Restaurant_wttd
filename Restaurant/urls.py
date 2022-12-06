from django.contrib import admin
from django.urls import include, path

from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index')
]

