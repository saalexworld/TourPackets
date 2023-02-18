from django.db import models
from django.contrib.auth import get_user_model
from slugify import slugify

User = get_user_model()


class Packet(models.Model):
    paket_category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='packets')
    slug = models.SlugField(max_length=200, primary_key=True, blank=True, unique=True)
    title = models.CharField(max_length=250) # название
    image = models.ImageField(upload_to='media/packet_image/')
    price = models.IntegerField() # цена
    description = models.TextField() # описание
    date_start = models.DateTimeField() # начало
    date_end = models.DateTimeField() # конец 
    availability = models.IntegerField() # cвободные места
    in_stock = models.BooleanField() # в наличии
    quantity = models.IntegerField()  # общее кол-во
    schedule = models.FileField()  #план тура
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='packets')

    def __str__(self):
        return f"{self.title}, {self.paket_category}" 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

class PacketImage(models.Model):
    packet_image = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='images')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/packet_image/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Hotel(models.Model):
    title = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    address = models.CharField(max_length=255)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='image')
    slug = models.SlugField(max_length=200, primary_key=True, blank=True, unique=True)

    def __str__(self):
        return f"{self.title}, {self.country}" 
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=30, primary_key=True, blank=True, unique=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save()

    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    