from rest_framework import serializers
from django.contrib.auth.models import User
from users.models import doctors,appointments
class user_serializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields='__all__'

class login_serializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields='email','password'

class docs_serializer(serializers.ModelSerializer):
    class Meta:
        model=doctors
        fields='__all__'
class appointment_serializer(serializers.ModelSerializer):
    class Meta:
        model=appointments
        fields='__all__'