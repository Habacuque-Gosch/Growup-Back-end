from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from .models import UserProfile





class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password']

    def validate_email(self, value):
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("Já existe um usuário com este e-mail.")
        return value

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)

    def create_user(self, validate_data):
        email = validate_data['email']
        username = validate_data['username']
        first_name = validate_data['full_name']
        password_value = validate_data['password']

        user = get_user_model()
        new_user = user.objects.create(email=email, username=username, first_name=first_name)
        password_user = make_password(password=password_value, salt=None, hasher='pbkdf2_sha256')
        # password_user_save = check_password(password=password_value, encoded=password_user)
        new_user.set_password(password_value)
        new_user.save()
        # token = Token.objects.create(user=new_user)
        # token.save()
        return new_user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email']

    # def get_user(self, token):
        # current_user = Token.objects.get(key=token)
        # return current_user

class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = get_user_model().EMAIL_FIELD  # por padrão é 'email', então funciona bem

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError({"email": "Usuário com este email não existe."})

        user = authenticate(username=user.username, password=password)

        if not user:
            raise serializers.ValidationError({"password": "Senha incorreta."})

        data = super().get_token(user)
        return {
            "refresh": str(data),
            "access": str(data.access_token),
        }

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["email"] = user.email
        return token

    def to_internal_value(self, data):
        return {
            "email": data.get("email"),
            "password": data.get("password")
        }


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'user', 'name', 'age', 'bio', 'sexual_orientation', 'photo', 'courses_save', 'preferences']
        read_only_fields = ['user']

