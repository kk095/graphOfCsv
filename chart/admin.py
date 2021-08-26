from django.contrib import admin
from .models import Csvfile,Check

# Register your models here.

@admin.register(Csvfile)
class form_admin(admin.ModelAdmin):
    list_display=['file']

@admin.register(Check)
class form_admin(admin.ModelAdmin):
    list_display=['name']

# Register your models here.
