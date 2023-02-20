from rest_framework import serializers

from .models import Like, Rating, Comment, LikeComment, Favorite


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
        representation['likes_count_to_comment'] = instance.liked.count()
        return representation


class RatingSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='user_set.count', read_only=True)

    class Meta:
        model = Rating
        fields = '__all__'

    def validate_rating(self, rating):
        if rating not in range(1, 6):
            raise serializers.ValidationError('Рейтинг не может быть меньше 1 и больше 5')
        return rating

    def validate(self, attrs):
        author = self.context.get("request").user
        length = (attrs.get("packet").ratings.filter(author=author)).count()
        if length > 0:
            raise serializers.ValidationError("Вы можете оставлять только 1 раз рейтинг")
        return super().validate(attrs)

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


class FavoriteSerializer(serializers.ModelSerializer):
    packet = serializers.ReadOnlyField(source='packet.title')
    author = serializers.ReadOnlyField(source='author.email')

    class Meta:
        model = Favorite
        fields = '__all__'
