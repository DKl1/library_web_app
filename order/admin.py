from django.contrib import admin
from .models import Order


class MembershipInline(admin.TabularInline):
    model = Order.book.through

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_book', 'user_email', 'created_at', 'plated_end_at', 'end_at')
    list_filter = ('id', 'book', 'user')

    inlines = [MembershipInline]
    def order_book(self, obj):
        return f"{obj.book.name}"

    def user_email(self, obj):
        return f"{obj.user.email}"


admin.site.register(Order, OrderAdmin)
