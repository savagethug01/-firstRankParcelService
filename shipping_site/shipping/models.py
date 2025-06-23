from django.db import models
import random
import string

def generate_shippment_code():
    return ''.join(str(random.randint(0, 8)) for _ in range(8))


class ShippingDetail(models.Model):
    STATUS_CHOICES = [
        ('processing', 'Processing'),
        ('in_transit', 'In Trransit'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]
    # SHIPPER DETAILS
    shipper_name = models.CharField(max_length=100, null=True, blank=True)
    shipper_address = models.TextField(max_length=100, null=True, blank=True)
    shipper_phone = models.CharField(max_length=100, null=True, blank=True)
    shipper_email = models.CharField(max_length=100, null=True, blank=True)

    #RECIEVER DETAILS
    receiver_name = models.CharField(max_length=100, null=True, blank=True)
    receiver_address = models.TextField(max_length=100, null=True, blank=True)
    receiver_phone = models.CharField(max_length=100, null=True, blank=True)
    receiver_email = models.CharField(max_length=100, null=True, blank=True)

    #SHIPMENT DETAILS
    origin = models.CharField(max_length=100, null=True, blank=True)
    shippment_destination = models.CharField(max_length=100, null=True, blank=True)
    carrier = models.CharField(max_length=100, null=True, blank=True)
    shippment_type = models.CharField(max_length=100, null=True, blank=True)

    
    #PACKAGE DETAILS
    contents =  models.TextField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)
    destination = models.CharField(max_length=255, default='Unknown Destination')
    code = models.CharField(max_length=10, unique=True, default=generate_shippment_code)
    expected_delivery_date = models.CharField(max_length=100, null=True, blank=True)
    departure_time = models.CharField(max_length=100, null=True, blank=True)
    pick_up_date = models.CharField(max_length=100, null=True, blank=True)
    pick_up_time = models.CharField(max_length=100, null=True, blank=True)
    comments = models.TextField(max_length=100, null=True, blank=True)


    def __str__(self):
        return f"{self.code} - {self.get_status_display()}"
