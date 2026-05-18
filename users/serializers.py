from rest_framework import serializers
from .models import User
from .utils import hash_password, check_password


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name')

    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data['password_hash'] = hash_password(password)
        return User.objects.create(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        try:
            user = User.objects.get(email=attrs['email'], is_active=True)
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials')

        if not check_password(attrs['password'], user.password_hash):
            raise serializers.ValidationError('Invalid credentials')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name")


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "password")

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        if password:
            instance.password_hash = hash_password(password)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
