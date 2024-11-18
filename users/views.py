# users/views.py
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.db.utils import IntegrityError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import authenticate, get_user_model

from portfolio.models import Portfolio
import logging

# Set up logging
logger = logging.getLogger(__name__)

User = get_user_model()

@api_view(['POST'])
def login(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')


         # Check if both email and password are provided
        if not email or not password:
            return Response(
                {"status": "error", "statusCode": 400, "message": "Email and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = authenticate(request, username=email, password=password)
        logger.info(f"Authenticated user: {user}")

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                "status": "success",
                "statusCode": 200,
                "token": str(refresh.access_token),
                "user": {
                    "name": f"{user.first_name} {user.last_name}",
                    "email": user.email
                }
            }, status=status.HTTP_200_OK)
        else:
            # Log a warning if authentication fails
            logger.warning(f"Login failed for email: {email}")
            return Response(
            {
                "status": "error",
                "statusCode": 401, # client's authentication credentials were invalid
                "message": "Invalid credentials",
                "errors": None  # Explicitly state no additional errors
            },
            status=status.HTTP_401_UNAUTHORIZED
        )
                
    except Exception as e:
        # Catch and log any unexpected errors during login
        logger.error(f"Error during login: {str(e)}")
        return Response(
            {"status": "error", 
             "statusCode": 500, 
             "message": "An error occurred during login."
             },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
@api_view(['POST'])
def signup(request):
    try:
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
                "status": "success",
                "statusCode": 201,
                "message": "User successfully registered",
                "token": str(refresh.access_token),
                "user": {
                    "name": f"{user.first_name} {user.last_name}",
                    "email": user.email
                }
            }, status=status.HTTP_201_CREATED)

        else:
            # Log the validation errors for debugging
            logger.warning(f"Signup failed: {serializer.errors}")
            return Response(
                {
                    "status": "error",
                    "statusCode": 400,
                    "message": "Invalid data provided.",
                    "errors": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
    except Exception as e:
        # Log any unexpected errors during signup
        logger.error(f"Error during signup: {str(e)}")
        return Response(
            {
                "status": "error",
                "statusCode": 500,
                "message": "An error occurred during signup."
            },
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
@api_view(['POST'])
def logout(request):
    try:
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({"detail": "Refresh token is required."}, status=status.HTTP_400_BAD_REQUEST)

        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)

    except Exception as e:
        logger.error(f"Error during logout: {str(e)}")
        return Response({"detail": "An error occurred during logout."}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getUsers(request):
    try:
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error fetching users: {str(e)}")
        return Response({"detail": "An error occurred while fetching users."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def validateUser(request):
    token = request.data.get('token')
    if not token:
        return Response({"detail": "Token is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        # Decode token to check validity
        access_token = AccessToken(token)
        user_id = access_token['user_id']
        user = User.objects.get(id=user_id)

        # If the token is valid, return user info
        return Response({"status": "success",
                         "user": {
                             "id": user.id,
                             "email": user.email,
                             "name": f"{user.first_name} {user.last_name}"
                         }}, status=status.HTTP_200_OK)
    
    except User.DoesNotExist:
        return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({"detail" : "Invalid or expired token"},  status=status.HTTP_401_UNAUTHORIZED)

