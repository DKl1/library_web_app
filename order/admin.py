from django.contrib import admin
from .models import Order


# admin.site.register(Order)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_book', 'user_email', 'created_at', 'plated_end_at', 'end_at')
    list_filter = ('id', 'book', 'user')

    def order_book(self, obj):
        return f"{obj.book.name}"

    def user_email(self, obj):
        return f"{obj.user.email}"


admin.site.register(Order, OrderAdmin)
