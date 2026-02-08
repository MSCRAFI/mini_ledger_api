from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Display the email, username, and status in the list view
    list_display = ("email", "username", "is_staff", "is_active")
    
    # Ordering by email since it's your primary identifier
    ordering = ("email",)
    
    # Fields to show when editing a user
    fieldsets = UserAdmin.fieldsets
    
    # Fields to show when creating a user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("email",)}),
    )