from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

from .models import Payment,Status , Favorite
from .serializers import PaymentSerializer, StatusSerializer, FavoriteSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]


    def get_serializer_context(self):
        return {
            'request': self.request,
            'user': self.request.user
        }


class PaymentItemViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class PaymentConfirmation(APIView):
    def post(self, request, pk):
        confirmation_code = request.data.get('confirmation_code')
        try:
            payment = Payment.objects.get(id=pk, status='PENDING')
            if payment.confirmation_code == confirmation_code:
                payment.status = 'PAID'
                payment.save()
                return Response(PaymentSerializer(payment).data)
            else:
                return Response({'error': 'Invalid confirmation code'}, status=status.HTTP_400_BAD_REQUEST)
        except Payment.DoesNotExist:
            return Response({'error': 'Payment not found'}, status=status.HTTP_404_NOT_FOUND)

            
# В этом примере мы создали новый APIView
# называется Подтверждение платежа, который обрабатывает логику подтверждения платежа.
# Когда запрос POST получен в этой конечной точке,
# код подтверждения извлекается из данного запроса и используется для получения
# платежного объекта из базы данных.
# Если платеж найден и код подтверждения совпадает,
# статус платежа обновляется «ОПЛАЧЕН». Если код подтверждения недействителен или платеж не найден,
# возвращается ответ об ошибке.
