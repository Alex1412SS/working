from django.contrib import admin
from .models import photos, Rating
from django.contrib.admin import ModelAdmin

admin.site.register(photos)
admin.site.register(Rating)
