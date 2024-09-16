# users/views.py
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.utils import IntegrityError

from portfolio.models import Portfolio

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if not username or not password:
        return Response({"detail": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return Response({"detail": "Invalid username"}, status=status.HTTP_401_UNAUTHORIZED)
    if not user.check_password(password):
        return Response({"detail": "Incorrect password"}, status=status.HTTP_401_UNAUTHORIZED)
    token, created = Token.objects.get_or_create(user=user)
    serializer = CustomUserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
            try:
                user = CustomUser.objects.create_user(
                    username=request.data['username'],
                    email=request.data['email'],
                    password=request.data['password']
                )
                token, created = Token.objects.get_or_create(user=user)

                # Initialize a portfolio for the new user
                Portfolio.objects.create(
                    uid=user,
                    total_value=10000,  # Initial total value
                    invested_value=0.00  # Initial invested value
                )

                user_serializer = CustomUserSerializer(instance=user)
                return Response({"token": token.key, "user": user_serializer.data})
            except IntegrityError:
                return Response({"detail": "A user with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def test_token(request):
    return Response({})
