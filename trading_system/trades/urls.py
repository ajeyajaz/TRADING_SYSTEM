
from django.urls import path
from .views import TradeListCreateAPIView

urlpatterns = [
    path('trades/', TradeListCreateAPIView.as_view() , name='trade-list-create'),
]
