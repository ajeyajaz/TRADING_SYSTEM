from rest_framework import serializers
from .models import Trade

import yfinance as yf

class TradeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Trade
        fields = "__all__"
        read_only_fields = ['id','timestamp']

    #==================validation==================================

    def validate_price(self, value): # price validation
        if value <= 0 :
            raise serializers.ValidationError('Must be greater than Zero.')
        return value
    
    def validate_ticker(self, value):  # ticker validation
        try:
            stack = yf.Ticker(value)
            info = stack.info

            if not info or "longName" not in info:
                raise serializers.ValidationError("Not a valid ticker")

        except Exception:
            raise serializers.ValidationError('Not a valid ticker')
        return value.upper()
    
    def validate_quantity(self , value): #quentity validation
        if value <= 0:
            raise serializers.ValidationError('Must be greater than zero')
        return value


    


