from rest_framework.serializers import ModelSerializer
from .models import Orders


class OrdersSerializer(ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"
