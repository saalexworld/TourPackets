from django.db import models
from django.contrib.auth import get_user_model

from Packets.models import Packet

User = get_user_model()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    packet = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.body


class Like(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    packet = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.packet}Liked by{self.author.email}'


class LikeComment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')
    is_liked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.comment}Liked by{self.author.email}'

class Rating(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveSmallIntegerField()
    packet = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self) -> str:
        return f'{self.rating} -> {self.packet}'
