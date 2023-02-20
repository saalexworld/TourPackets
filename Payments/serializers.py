from rest_framework import serializers

from .models import Payment, PaymentItem, Status#, Favorite


class PaymentItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentItem
        fields = ['packet', 'quantity']


class PaymentSerializer(serializers.ModelSerializer):
    items = PaymentItemSerializer(many=True)
    confirmation_code = serializers.CharField()


    class Meta:
        model = Payment
        fields = ['id', 'created_at', 'total_sum', 'items','confirmation_code']

    def create(self, validated_data):
        items = validated_data.pop('items')
        validated_data['author'] = self.context.get('user')
        payment = super().create(validated_data)
        total_sum = 0
        payment_items = []
        for item in items:
            payment_items.append(
                PaymentItem(
                payment=payment, 
                packet=item['packet'],
                quantity=item['quantity']
            ))

            total_sum += item['packet'].price * item['quantity']
        PaymentItem.objects.bulk_create(payment_items)
        payment.total_sum = total_sum
        payment.save()
        return payment


# class FavoriteSerializer(serializers.ModelSerializer):
#     product = serializers.ReadOnlyField()
#     author = serializers.ReadOnlyField(source='author.email')


#     class Meta:
#         model = Favorite
#         fields = '__all__'
        

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
        