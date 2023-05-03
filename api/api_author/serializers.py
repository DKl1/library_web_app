from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class AuthorSerializerIdName(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name') # replace 'name' with the name of the field that stores the author name in your Author model
