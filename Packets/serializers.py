from rest_framework import serializers
from .models import Packet, PacketImage, Category, Hotel


class PacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packet
        fields = '__all__'
    
    
    

class PacketImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PacketImage
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class HotelSerializer(serializers.ModelSerializer):

     class Meta:
        model = Hotel
        fields = '__all__'
