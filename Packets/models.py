from django.db import models
from django.contrib.auth import get_user_model
# from slugify import slugify

User = get_user_model()


class Packet(models.Model):
    paket_category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='packets')
    date_start = models.DateTimeField() 
    date_end = models.DateTimeField() 
    price = models.IntegerField() 
    quantity = models.IntegerField()
    from_packet = models.CharField(max_length=100) #departure
    to_packet = models.CharField(max_length=100) #arrival
    description = models.TextField() 
    schedule = models.FileField()  
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='packets')
    availability = models.IntegerField() 
    in_stock = models.BooleanField() 
    image = models.ImageField(upload_to='media/packet/')
    title = models.CharField(max_length=250) 
    day_1 = models.TextField()
    day_2 = models.TextField()
    day_3 = models.TextField()
    day_4 = models.TextField()
    day_5 = models.TextField()
    day_6 = models.TextField()
    day_7 = models.TextField()

    def __str__(self):
        return f"{self.title}, {self.paket_category}"
    
    # slug = models.SlugField(max_length=200, primary_key=True, blank=True, unique=True)
    # настроить по возможности
 
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save()


class PacketImage(models.Model):
    packet_image = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='images')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/packet_image/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
class Hotel(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/hotel/')
    address = models.CharField(max_length=255)
    stars = models.CharField(max_length=255)
    breakfast = models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return f"{self.title}, {self.stars}" 
    
    # slug = models.SlugField(max_length=200, primary_key=True, blank=True, unique=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save()


class HotelImage(models.Model):
    hotel_image = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/hotel_image/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # beaches 
    # iconic cities
    # deserts
    # mountains
    # skiing
    # camping
    # tropic

    # slug = models.SlugField(max_length=30, primary_key=True, blank=True, unique=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save()
    