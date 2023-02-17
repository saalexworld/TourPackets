from django.db import models
from Packets.models import Packet
from django.contrib.auth import get_user_model


User = get_user_model()

class Payment(models.Model):
    author = models.ForeignKey(User, related_name='payments', on_delete=models.CASCADE)
    packet = models.ForeignKey(Packet, related_name='PaymentItem', on_delete=models.CASCADE)
    total_sum = models.DecimalField(max_digits=10,decimal_places=2,default=0) 
    payments = [
                ('Card', 'Card'),
                ('Cash', 'Cash'),
            ]
    payment = models.CharField(max_length=4, choices=payments)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return f'Payment ID: {self.pk}'


class PaymentItem(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='items')
    packet = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='packet_item')
    quantity = models.PositiveIntegerField(default=1)

# class Favorite(models.Model):
#     author = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='favorites'
#     )
#     packet = models.ForeignKey(
#         Packet, on_delete=models.CASCADE, related_name='favorites'
#     )
#     is_favorite = models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return f'{self.is_favorite} favorite by {self.author.email}'

# class Ticket(models.Model):
#     info = models.CharField(max_length=255)
#     ticket_payments = models.ForeignKey(Payment, on_delete=models.CASCADE, related_name='ticket')
    

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'
