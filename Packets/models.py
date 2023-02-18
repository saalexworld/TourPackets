from django.db import models
from slugify import slugify


class Packet(models.Model):
    paket_category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='pakets')
    paket_title = models.CharField(max_length=250) # название
    image = models.ImageField(upload_to='media/packet_image/')
    price = models.IntegerField() # цена
    description = models.TextField() # описание
    date_start = models.DateTimeField() # начало
    date_end = models.DateTimeField() # конец 
    availability = models.IntegerField() # cвободные места
    in_stock = models.BooleanField() # в наличии
    quantity = models.IntegerField()  # общее кол-во
    schedule = models.FileField()  #план тура
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='pakets')

    def __str__(self):
        return f"{self.paket_title}, {self.paket_category}" 


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

    def __str__(self):
        return f"{self.title}, {self.country}" 


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True, verbose_name='Название категории')
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
    