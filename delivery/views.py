from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Orders
from .serializer import OrdersSerializer
from rest_framework import status

# Create your views here.


class OrdersViews(APIView):
    def get(self, request):
        all_orders = Orders.objects.all()

        serialized_data = OrdersSerializer(data=all_orders, many=True)

        serialized_data.is_valid()

        return Response(data=serialized_data.data)

    def post(self, request):
        serialized_data = OrdersSerializer(data=request.data)

        if serialized_data.is_valid():
            serialized_data.save()

            return Response(data=serialized_data.data)

        return Response({"error": serialized_data.errors})

    def delete(self, request):
        id = request.data["id"]
        try:
            Orders.objects.get(id=id)

            return Response({"status": "Success!"}, status=status.HTTP_200_OK)

        except:
            return Response({"status": "Not Found"}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request):
        orders = Orders.objects.get(id=request.data["id"])

        serialized_data = OrdersSerializer(orders, data=request.data, partial=True)

        if serialized_data.is_valid():
            serialized_data.save()

            return Response(data=serialized_data.data)

        return Response({"error": serialized_data.errors})


class SingleOrder(APIView):
    def get(self, request, id):
        orders_data = Orders.objects.get(id=id)

        return Response(
            data={
                "id": orders_data.id,
                "name": orders_data.name,
                "type_of_meal": orders_data.type_of_meal,
                "meal": orders_data.order,
                "count_diners": orders_data.count_diners,
                "phone": orders_data.phone,
                "region_name": orders_data.region_name,
                "adress": orders_data.adress,
                "time": orders_data.time,
                "comment": orders_data.comment,
                "createrd_at": orders_data.created_at,
                "updated_at": orders_data.updated_at,
            }
        )
