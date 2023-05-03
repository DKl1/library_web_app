from rest_framework import serializers
from .models import Order
from ..api_book.serializers import BookSerializer
from ..api_book.models import Book


class OrderSerializer(serializers.ModelSerializer):
    book_names = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ['id', 'book', 'user', 'created_at', 'end_at', 'plated_end_at', 'book_names', 'is_prepared_at',
                  'received_by_user_at', ]

    def get_book_names(self, obj):
        book_ids = obj.book.values_list('id', flat=True)
        books = Book.objects.filter(id__in=book_ids)
        return BookSerializer(books, many=True).data
