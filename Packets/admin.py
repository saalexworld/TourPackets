from django.contrib import admin

from .models import Packet, Category, PacketImage, Hotel


class PacketImageInline(admin.TabularInline):
    model = PacketImage


class PacketAdmin(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['title', 'paket_category', 'price']
    search_fields = ['title' ,'packet_category', 'description']
    inlines = [PacketImageInline]


admin.site.register(Packet, PacketAdmin)

admin.site.register(Category)

admin.site.register(PacketImage)

admin.site.register(Hotel)
