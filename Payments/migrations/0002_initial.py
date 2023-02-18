# Generated by Django 4.1.7 on 2023-02-18 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Packets', '0001_initial'),
        ('Payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='payment',
            name='packet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PaymentItem', to='Packets.packet'),
        ),
        migrations.AddField(
            model_name='favorite',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='favorite',
            name='packet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='Packets.packet'),
        ),
    ]