from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.utils.translation import gettext_lazy as _

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    list_filter = ['is_active', 'is_staff']
    ordering = ['email']
    search_fields = ['email', 'first_name', 'last_name']

    # Remove 'groups' and 'user_permissions' from filter_horizontal
    filter_horizontal = []  # No need to filter anything if you're not using permissions or groups

    # Adjust fieldsets to match your CustomUser model
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'phoneNumber')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff')}),
        (_('Important dates'), {'fields': ('dateJoined',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
