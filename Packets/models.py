from django.db import models
from django.contrib.auth import get_user_model
# from slugify import slugify

User = get_user_model()


class Packet(models.Model):
    # id = models.PositiveSmallIntegerField(primary_key=True, unique=True)
    packet_category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='packets')
    date_start = models.DateField(blank=True, null=True) 
    date_end = models.DateField(blank=True, null=True) 
    price = models.IntegerField(blank=True, null=True) 
    quantity = models.IntegerField(blank=True, null=True)
    departure = models.CharField(max_length=100, blank=True) 
    arrival = models.CharField(max_length=100, blank=True) 
    description = models.TextField(blank=True, null=True) 
    schedule = models.FileField(blank=True, null=True)  
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE, related_name='packets')
    availability = models.IntegerField(blank=True, null=True) 
    in_stock = models.BooleanField(blank=True, null=True) 
    image = models.ImageField(upload_to='media/packet/', blank=True, null=True)
    title = models.CharField(max_length=250) 
    day_1 = models.TextField(blank=True, null=True)
    day_2 = models.TextField(blank=True, null=True)
    day_3 = models.TextField(blank=True, null=True)
    day_4 = models.TextField(blank=True, null=True)
    day_5 = models.TextField(blank=True, null=True)
    day_6 = models.TextField(blank=True, null=True)
    day_7 = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title}, {self.packet_category}"
    
    # slug = models.SlugField(max_length=200, primary_key=True, blank=True, unique=True)
    # настроить по возможности
 
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save()


class PacketImage(models.Model):
    # id = models.PositiveSmallIntegerField(primary_key=True, unique=True)
    packet_image = models.ForeignKey(Packet, on_delete=models.CASCADE, related_name='images')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/packet_image/', blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)

    
class Hotel(models.Model):
    # id = models.PositiveSmallIntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/hotel/', blank=True)
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
    # id = models.PositiveSmallIntegerField(primary_key=True, unique=True)
    hotel_image = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='images')
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='media/hotel_image/', blank=True)
    created_at = models.DateField(auto_now_add=True, blank=True)
    updated_at = models.DateField(auto_now=True, blank=True)


# CATEGORY_TOUR = [
#         ('BEACHES', 'beaches',),
#         ('ICONIC CITIES', 'iconic cities',),
#         ('DESERTS', 'deserts',),
#         ('MOUNTAINS', 'mountains',),
#         ('SKIING', 'skiing',),
#         ('CAMPING', 'camping',),
#         ('TROPIC', 'tropic', )
#     ]
# choices=CATEGORY_TOUR (добавить в поле для использования)

class Category(models.Model):
    # id = models.PositiveSmallIntegerField(primary_key=True, unique=True)
    title = models.CharField(max_length=255)
    descriptions = models.TextField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    # slug = models.SlugField(max_length=30, primary_key=True, blank=True, unique=True)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save()
    