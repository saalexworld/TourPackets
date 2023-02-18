from django.contrib import admin

from .models import Packet, Category, PacketImage, Hotel


class PacketImageInline(admin.TabularInline):
    model = PacketImage


class PacketAdmin(admin.ModelAdmin):
    list_filter = ['paket_title']
    list_display = ['paket_title', 'paket_category', 'price', 'id']
    search_fields = ['paket_title' ,'packet_category', 'description']
    inlines = [PacketImageInline]


admin.site.register(Packet, PacketAdmin)

admin.site.register(Category)

admin.site.register(PacketImage)

admin.site.register(Hotel)


    

