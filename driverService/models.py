from django.db import models

class Driver(models.Model):
    driver_id = models.IntegerField(primary_key = True)
    driver_status = models.CharField(max_length = 12, default='default_value_here')
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    vehicle_number = models.CharField(max_length=20)
    vehicle_model = models.CharField(max_length=255)
    track_url = models.URLField(null=True, blank=True)

class DriverVerificationCode(models.Model):
    phone_number = models.CharField(max_length=12, null=False)
    code = models.CharField(max_length=6, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('expired', 'Expired'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

class DriverRide(models.Model):
    ride_id = models.AutoField(primary_key = True)
    customer_id = models.IntegerField(null=True, blank=True)
    customer_ride_id = models.IntegerField(null=True, blank=True)
    ride_date_time = models.DateTimeField()
    driver = models.ForeignKey(Driver, to_field='driver_id',on_delete=models.CASCADE)
    ride_type = models.CharField(max_length=20, choices=[("Sharing", "Sharing"), ("Private", "Private")])


class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,blank=True,null=True)
    customer_id = models.IntegerField()
    customer_ride_id = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    drop_priority = models.IntegerField(null=True, blank=True)
    pickup_address = models.CharField(max_length=500,blank=True,null=True)
    drop_address = models.CharField(max_length=500,blank=True,null=True)
    driver = models.ForeignKey(Driver,to_field='driver_id', on_delete=models.CASCADE)
    ride_date_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    customer_ride_status = models.CharField(max_length=20, choices=[("Upcoming", "Upcoming"), ("Ongoing", "Ongoing"),
                                                                    ("Cancelled", "Cancelled"), ("Completed", "Completed")], null=True, blank=True)

    customer_lat_pickup = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    customer_lon_pickup = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    customer_lat_drop = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    customer_lon_drop = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

class Copassenger(models.Model):
    co_passenger = models.ForeignKey(Customer, to_field='id', on_delete=models.CASCADE)
    ride = models.ForeignKey(DriverRide, to_field='ride_id', on_delete=models.CASCADE)


class RideCategory(models.Model):
    customer_cab_ride_id = models.IntegerField(null=True, blank=True)
    cab_ride_category = models.CharField(max_length=255)



















