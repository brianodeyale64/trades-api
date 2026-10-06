from rest_framework import serializers
from app.models import Trade

class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = "__all__"

    def validate_shares(self, value):
        if value < 1 or value > 100:
            raise serializers.ValidationError("Shares must be between 1 and 100.")
        return value

    def validate_type(self, value):
        if value not in ["buy", "sell"]:
            raise serializers.ValidationError("Type must be in 'buy' or 'sell'." )
        return value
