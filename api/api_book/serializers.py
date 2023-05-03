from rest_framework import serializers
from .models import Book
from ..api_author.serializers import AuthorSerializerIdName


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializerIdName(many=True, read_only=True)

    class Meta:
        model = Book
        fields = '__all__'
