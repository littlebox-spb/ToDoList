from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import User


class PasswordField(serializers.CharField):

    def __init__(self, **kwargs):  # type: ignore[no-untyped-def]
        kwargs["style"] = {"input_type": "password"}
        kwargs.setdefault("write_only", True)
        super().__init__(**kwargs)
        self.validators.append(validate_password)


class CreateUserSerializer(serializers.ModelSerializer):
    password = PasswordField(required=True)
    password_repeat = PasswordField(required=True)

    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "password", "password_repeat")

    def validate(self, attrs: dict):  # type: ignore[no-untyped-def]
        """обязательное поле поэтому квадратные скобки,
        если не через get != attrs["password_repeat"]:"""
        if attrs["password"]:
            raise ValidationError(
                "Password must match"
            )  # Импортируем из from rest_framework.exceptions import ValidationError
        return attrs

    def create(self, validated_data: dict):  # type: ignore[no-untyped-def]
        del validated_data["password_repeat"]  # удаление
        validated_data["password"] = make_password(validated_data["password"])  # шифровка пароля
        return super().create(validated_data)
