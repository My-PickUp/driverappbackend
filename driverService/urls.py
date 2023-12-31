from django.urls import path
from driverService import views

urlpatterns = [
    path('fetchDrivers/<str:phone>/', views.get_drivers, name='get-drivers'),
    path('createDrivers/', views.create_driver, name='create-driver'),
    path('generateOtp/', views.generate_otp, name='generate-otp'),
    path('verifyOtp/', views.verify_otp, name='verify-otp'),
    path('getDriverDetails/', views.get_driver_details, name='get-driver-details'),
    path('getCustomerDetails/',views.get_customer_details, name='get-upcoming-rides'),
    path('rideDetailsUpload/', views.form_upload_response, name='ride-details-upload'),
    path('getPrivateRides/<int:driver_id>/', views.get_upcoming_private_rides, name='get-upcoming-private-rides'),
    path('getSharingRides/<int:driver_id>/', views.get_upcoming_sharing_rides, name='get-upcoming-sharing-rides'),
    path('startRide/', views.start_ride, name='start-ride'),
    path('awake/', views.awake, name='awake'),
]