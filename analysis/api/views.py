""" This module includes views for the urls
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from analysis.models import StockPrices
from analysis.api.serializers import (
    StockPricesSerializer,
    TopVolumeSerializer
)

class PercentageChangeView(APIView):
    """ View for Returning Percentage Changes
        Url : /analysis/percentages/
    """
    def post(self, request, format=None):
        """ Function definition for method POST
        """
        stocks = StockPrices.objects.filter(stock_id__name=request.data['name'])
        serializer = StockPricesSerializer(stocks, many=True)
        return Response(serializer.data)

class TopVolumesView(APIView):
    """ View for Returning Top 5 volumes of given StockName
        Url : /analysis/topvolumes/
    """
    def post(self, request, format=None):
        """ Function definition for method POST
        """
        tops = StockPrices.objects.filter(
            stock_id__name=request.data['name']).order_by('-stock_volume')[:5]
        serializer = TopVolumeSerializer(tops, many=True)
        return Response(serializer.data)
