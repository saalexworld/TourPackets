
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Payment,Status  #Favorite, Ticket
from .serializers import PaymentSerializer, StatusSerializer #FavoriteSerializer, TicketSerializer
from rest_framework import viewsets

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

# class FavoriteViewSet(viewsets.ModelViewSet):
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteSerializer


# class TicketViewSet(viewsets.ModelViewSet):
#     queryset = Ticket.objects.all()
#     serializer_class = TicketSerializer

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer