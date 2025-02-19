from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.authtoken.models import Token



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

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
        token = Token.objects.create(user=new_user)
        token.save()
        return new_user

class GetUserByToken(serializers.ModelSerializer):
    class Meta: 
        model = get_user_model()
        fields = '__all__'

    # def get_user(self, token):
        # current_user = Token.objects.get(key=token)
        # return current_user

