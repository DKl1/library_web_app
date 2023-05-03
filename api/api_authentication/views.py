from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated


class CustomUserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAuthenticated]


class UserDetailView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # permission_classes = [IsAuthenticated]
    lookup_field = 'middle_name'


# class SignUpView(APIView):
#     serializer_class = CustomUserSerializer
#
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user_data = serializer.save()
#             return Response(user_data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.contrib.auth.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .csrf_exempt import csrf_exempt_class

@csrf_exempt_class
class SignUpView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name', '')
        last_name = request.data.get('last_name', '')
        middle_name = request.data.get('middle_name', '')

        if not email or not password:
            return Response({'error': 'Email and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user(email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.middle_name = middle_name
        user.save()

        # Get the token for the created user
        token_serializer = TokenObtainPairSerializer(data={'email': email, 'password': password})
        if token_serializer.is_valid():
            tokens = token_serializer.validated_data
            return Response({'refresh': str(tokens['refresh']), 'access': str(tokens['access'])},
                            status=status.HTTP_201_CREATED)

        return Response({'error': 'Could not generate tokens'}, status=status.HTTP_400_BAD_REQUEST)
