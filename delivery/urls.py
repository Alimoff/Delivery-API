from django.urls import path
from .views import OrdersViews

urlpatterns = [
    path("list/", OrdersViews.as_view()),
]
