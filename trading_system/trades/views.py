from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView
from .models import Trade
from .serializers import TradeSerializer

from datetime import datetime

#retreveing  adn creatiion of Trades
class TradeListCreateAPIView(ListCreateAPIView):

    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
        
    def get_queryset(self):
        queryset =  super().get_queryset()

        # Ticker filtering
        ticker = self.request.query_params.get('ticker')

        if ticker:
            queryset = queryset.filter(ticker__iexact=ticker.upper())

        # Date  filtering
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')

        if start_date:

            try:
                start_date = datetime.strptime(start_date, '%Y-%m-%d')
                queryset= queryset.filter(timestamp__date__gte=start_date)
            except Exception:
                pass

        if end_date:

            try:
                end_date = datetime.strptime(end_date, '%Y-%m-%d')
                queryset = queryset.filter(timestamp__date__lte=end_date)
            except Exception:
                pass

        return queryset
    



        
        


   

        

        
    

    
