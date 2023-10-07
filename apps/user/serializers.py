from .models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = {'id', 'username', 'email', 'password',
                 'first_name', 'last_name', 'bio', 'image', }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data('password'))
        user.save()
        return user


class ChangePasswordSerializer(serializers.Serializer):
    password1 = serializers.CharField(
        require=True, write_only=True, min_length=5)
    password2 = serializers.CharField(
        require=True, write_only=True, min_length=5)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError("passwords don't match")
        else:
            return data
