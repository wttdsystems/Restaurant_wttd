from rest_framework.viewsets import ModelViewSet

from core.models import Comand, Item, Waiter

from .serializers import ComandSerializer, ItemSerializer, WaiterSerializer


class ComandViewset(ModelViewSet):
    queryset = Comand.objects.all()
    serializer_class = ComandSerializer


class ItemViewset(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class WaiterViewset(ModelViewSet):
    queryset = Waiter.objects.all()
    serializer_class = WaiterSerializer
