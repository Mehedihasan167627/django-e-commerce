from rest_framework import serializers
from products.models import Order, Product 

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product 
        fields=[
            'id','title','image','price','discount_price','sub_category',
            'created_at',"updated"
        ]
 

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product 
        fields=[
            'id','title','image','price','discount_price','description','men_or_women',
            'sale_count','sub_category','multiple_image',
            'created_at',"updated"
        ]


class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

class OrderCreateSerializer(serializers.Serializer):
    product_id_and_quantity=serializers.CharField(max_length=10)
    
    class Meta:
        fields=["product_id_and_quantity"]


