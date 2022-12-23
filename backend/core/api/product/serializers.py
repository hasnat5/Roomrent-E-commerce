from rest_framework import serializers
from seller.models.Product import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['namaProduct','keterangan','owner','gambar']