# users/serializers.py
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'id', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}
    
    def validate(self, data):
        password = data.get('password')
        print(password)
        # Create a temporary user instance to pass to validate_password
        user = User(
            email=data.get('email'),
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
        )
        
        try:
            validate_password(password, user=user)
        except ValidationError as e:
            print("Validation error details:", e.messages)  # Debugging output
            raise serializers.ValidationError({"password": e.messages})
        return data
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

