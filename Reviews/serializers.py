from rest_framework import serializers
from .models import Like, Rating, Comment,LikeComment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    
    class Meta:
        model = Comment
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Rating
        fields = '__all__'

    def validate_rating(self, rating):
        if  0 > rating > 5:
            raise serializers.ValidationError(
                'rating must be beetween 0 and 5'
            )
        return rating

    
    def validate_product(self, product):
        if  self.Meta.model.objects.filter(product=product):
            raise serializers.ValidationError(
                'Vy uje ostavili otzyv na danniy kommentariy'
            )
        return product

    
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        rating = Rating.objects.create(author=user, **validated_data)
        return rating
    

class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    product = serializers.ReadOnlyField()

    class Meta:
        model = Like
        fields = '__all__'


class LikeCommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    comment = serializers.ReadOnlyField()

    class Meta:
        model = LikeComment
        fields = '__all__'

    
    def create(self, validated_data):
        requests = self.context.get('request')
        user = requests.user
        like_comment = LikeComment.objects.create(author=user, **validated_data)

        return like_comment

