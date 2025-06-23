from django.contrib import admin
from .models import ShippingDetail

@admin.register(ShippingDetail)
class ShippingDetailAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'status', 'origin', 'shippment_destination', 
        'shipper_name', 'receiver_name', 'expected_delivery_date'
    )
    
    fieldsets = (
        ('Shipment Info', {
            'fields': (
                'code', 'status', 'origin', 'destination', 'carrier', 
                'shippment_type', 'expected_delivery_date', 'departure_time'
            )
        }),
        ('Shipper Information', {
            'fields': (
                'shipper_name', 'shipper_address', 'shipper_phone', 'shipper_email', 'shippment_destination'
            )
        }),
        ('Receiver Information', {
            'fields': (
                'receiver_name', 'receiver_address', 'receiver_phone', 'receiver_email'
            )
        }),
        ('Package & Tracking Details', {
            'fields': (
                'contents', 'pick_up_date', 'pick_up_time', 'comments'
            )
        }),
    )
