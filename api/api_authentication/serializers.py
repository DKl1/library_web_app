from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import CustomUser, ROLE_CHOICES


class CustomUserSerializer(serializers.ModelSerializer):
    # role = serializers.ChoiceField(choices=ROLE_CHOICES, source='get_role_display')
    role = serializers.ChoiceField(choices=ROLE_CHOICES)
    class Meta:
        model = CustomUser
        fields = '__all__'

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        refresh = RefreshToken.for_user(user)

        return {
            'user': self.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

