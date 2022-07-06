from django.urls import path
from .views import OrdersViews, SingleOrder

urlpatterns = [
    path("list/", OrdersViews.as_view()),
    path("list/<int:id>/", SingleOrder.as_view()),
    path("cook/", OrdersViews.as_view()),
]
