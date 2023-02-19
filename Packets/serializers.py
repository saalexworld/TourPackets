from django.db.models import Avg
from rest_framework import serializers

from .models import Packet, PacketImage, Category, Hotel
from Reviews.serializers import RatingSerializer, CommentSerializer, \
FavoriteSerializer
from Reviews.models import Comment


class PacketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Packet
        fields = '__all__'

    def validate_price(self, price): 
        if price < 0:
            raise serializers.ValidationError('Цена не может быть отрицательной')
        return price
    
    def to_representation(self, instance): 
        representation = super().to_representation(instance)
        representation['ratings'] = RatingSerializer(instance.ratings.all(), many=True).data 
        representation['ratings'] = instance.ratings.aggregate(Avg('rating'))['rating__avg'] 
        representation['comments'] = CommentSerializer(Comment.objects.filter(packet=instance.pk),many=True).data 
        representation['comments'] = [i.body for i in instance.comments.all()]
        representation['ratings'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        representation['likes_count'] = instance.likes.count()
        representation['favorites'] = FavoriteSerializer(instance.favorites.all(), many=True).data 
        return representation


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
