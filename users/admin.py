from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # You can configure fields and options here as needed

admin.site.register(CustomUser, CustomUserAdmin)
