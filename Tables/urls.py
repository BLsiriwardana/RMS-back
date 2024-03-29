# Import your view function
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import qr_code_api

# Define URL patterns
urlpatterns = [
    # Other URL patterns
    path('qrscan/', qr_code_api, name='qr_code_api'),
]
