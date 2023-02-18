from rest_framework import serializers

from .models import Like, Rating, Comment, LikeComment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    
    class Meta:
        model = Comment
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context.get('request') 
        user = request.user 
        comment = Comment.objects.create(author=user, **validated_data)
        return comment

    def to_representation(self, instance): 
        representation = super().to_representation(instance)
        representation['likes_count'] = instance.likes.count()
        return representation


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Rating
        fields = '__all__'

    def validate_rating(self, rating):
        if  0 > rating > 5:
            raise serializers.ValidationError(
                'Рейтиенг не может быть меньще 0 и больше 5'
            )
        return rating

    def validate_packet(self, packet):
        if  self.Meta.model.objects.filter(packet=packet):
            raise serializers.ValidationError(
                'Вы уже оставляли рейтинг'
            )
        return packet

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        rating = Rating.objects.create(author=user, **validated_data)
        return rating
    

class LikeSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.email')
    packet = serializers.ReadOnlyField()

    class Meta:
        model = Like
        fields = '__all__'
    
    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user 
        like = Like.objects.create(author=user, **validated_data)
        return like


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
