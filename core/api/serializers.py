from rest_framework.serializers import ModelSerializer

from core.models import Comand, Item, Waiter


class ComandSerializer(ModelSerializer):
    class Meta:
        model = Comand
        fields = '__all__'


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class WaiterSerializer(ModelSerializer):
    class Meta:
        model = Waiter
        fields = '__all__'

        