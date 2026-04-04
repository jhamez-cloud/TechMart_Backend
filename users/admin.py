'''Documentation String'''
from unfold.admin import ModelAdmin
from django.contrib import admin
from .models import UserProfile

# Register your models here.
@admin.register(UserProfile)

class UserProfileAdmin(ModelAdmin):
    '''Documentation String'''
    list_display = ["firebase_uid","profile_pic","user_name","email","phone"]
    list_per_page = 10
    ordering = ("firebase_uid",)
    search_fields = ("user_name",)
