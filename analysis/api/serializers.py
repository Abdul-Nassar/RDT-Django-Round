""" Module includes serializers for views
"""
import locale
from rest_framework.serializers import (
    ModelSerializer, SerializerMethodField
)
from analysis.models import (
    StockName, StockPrices
)

class StockNameSerializer(ModelSerializer):
    """ Serializer for StockName model, it returns all fields of StockName model
    """
    class Meta:
        model = StockName
        fields = '__all__'

class StockPricesSerializer(ModelSerializer):
    """ Serializer for StockPrices model, it Used for returning percentage changes
    """
    stock_id = StockNameSerializer
    change = SerializerMethodField('get_percentage')
    date = SerializerMethodField('get_stock_date')

    def get_percentage(self, obj):
        """ Returns percentage change of stock_open and stock_close fields of StockPrices model
        """
        changes = "%.2f" %((
            (float(obj.stock_close - obj.stock_open)) / float(obj.stock_open)) * 100)
        return changes

    def get_stock_date(self, obj):
        """ Returns stock_date field of StockPrices model as 'March 17, 2017'
        """
        return obj.stock_date.strftime("%B %d, %Y")

    class Meta:
        model = StockPrices
        fields = [
            'stock_open', 'stock_close',
            'date', 'change'
        ]

class TopVolumeSerializer(ModelSerializer):
    """ Serializer for StockPrices model, it Used for returning Top Stock volumes
    """
    stock_id = StockNameSerializer
    date = SerializerMethodField('get_stock_date')
    Volume = SerializerMethodField('get_volume')

    def get_stock_date(self, obj):
        """ Returns stock_date field of StockPrices model as 'March 17, 2017'
        """
        return obj.stock_date.strftime("%B %d, %Y")

    def get_volume(self, obj):
        """ Returns stock_volume field of StockPrices model as '4,92,19,686'
        """
        locale.setlocale(locale.LC_ALL, 'en_IN.UTF-8')
        return locale.format("%d", obj.stock_volume, grouping=True)

    class Meta:
        model = StockPrices
        fields = [
            'date', 'Volume'
        ]
