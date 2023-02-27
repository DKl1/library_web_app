from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# admin.site.register(CustomUser)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'middle_name', 'created_at', 'updated_at', 'role', 'id')
    list_filter = ('id', 'role')


admin.site.register(CustomUser, CustomUserAdmin)
