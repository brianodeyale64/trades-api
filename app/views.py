from django.shortcuts import render
from rest_framework import viewsets
from app.models import Trade
from app.serializers import TradeSerializer


class TradeViewSet(viewsets.ModelViewSet):
    serializer_class = TradeSerializer
    http_method_names = ["get", "post"]

    def get_queryset(self):
        trades = Trade.objects.all().order_by("id")

        trade_type = self.request.query_params.get("type")
        if trade_type is not None:
            trades = trades.filter(type=trade_type)

        user_id = self.request.query_params.get("user_id")
        if user_id is not None:
            trades = trades.filter(user_id=user_id)

        return trades