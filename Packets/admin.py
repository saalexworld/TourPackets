from django.contrib import admin

from .models import Packet, Category, PacketImage, Hotel, HotelImage


class PacketImageInline(admin.TabularInline):
    model = PacketImage


class PacketAdmin(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['title', 'paket_category', 'price']
    search_fields = ['title' ,'packet_category', 'description']
    inlines = [PacketImageInline]

admin.site.register(Packet, PacketAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['title']
    # list_display = ['title', 'paket_category', 'price']
    # search_fields = ['title' ,'packet_category', 'description']

admin.site.register(Category, CategoryAdmin)


class PacketImageAdmin(admin.ModelAdmin):
    list_display = ['packet_image', 'is_active', 'created_at']

admin.site.register(PacketImage)


class HotelImageInline(admin.TabularInline):
    model = HotelImage


class HotelAdmin(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['title', 'address', 'stars']
    search_fields = ['stars']
    inlines = [HotelImageInline]

admin.site.register(Hotel, HotelAdmin)


class HotelImageInline(admin.TabularInline):
    list_display = ['hotel_image', 'created_at', 'is_active']

admin.site.register(HotelImage)
