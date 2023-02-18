from django.contrib import admin
from .models import Payment, PaymentItem, Status

admin.site.register(Payment)

admin.site.register(PaymentItem)

admin.site.register(Status)