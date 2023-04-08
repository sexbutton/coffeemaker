from rest_framework import serializers
from .views import Product

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'category', 'average_consumption')
