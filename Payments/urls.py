from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet, PaymentConfirmation


router = DefaultRouter()
router.register('payments', PaymentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('payments/<int:pk>/confirm/', PaymentConfirmation.as_view(), name='payment-confirmation'),
]
