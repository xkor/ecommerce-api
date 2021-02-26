from django.contrib.auth import get_user_model
from rest_framework import serializers, validators
from rest_framework.authtoken.models import Token
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=64, read_only=True)
    password = serializers.CharField(max_length=200, write_only=True)
    password2 = serializers.CharField(max_length=200, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'phone_number', 'token', 'password', 'password2')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        password2 = validated_data.pop('password2', None)
        phone_number = validated_data.pop('phone_number', None)
        if password != password2:
            raise validators.ValidationError({'message': 'password not matched!'})
        if User.objects.filter(phone_number=phone_number).count() > 0:
            raise validators.ValidationError({'message': 'User already exist'})

        user = User.objects.create(phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user
