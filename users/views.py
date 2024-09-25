# users/views.py
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.db.utils import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from portfolio.models import Portfolio

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, username=email, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access' : str(refresh.access_token),
        }, status=status.HTTP_200_OK)
    else:
        return Response({"detail": "Invalid credentials"})

@api_view(['POST'])
def signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        refresh = RefreshToken.for_user(user)

            # Initialize a portfolio for the new user
        Portfolio.objects.create(
            uid=user,
            total_value=10000,  # Initial total value
            invested_value=0.00  # Initial invested value
        )

        return Response({
            'refresh' : str(refresh),
            'access' : str(refresh.access_token),
            'userName': request.data.get('email')
        }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['Post'])
def logout(request):
    try:
        refresh_token = request.data['refresh']
        token = RefreshToken(refresh_token)
        token.blacklist() 

        return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def test_token(request):
    return Response({})
