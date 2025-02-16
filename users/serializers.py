from rest_framework import serializers
from django.contrib.auth import get_user_model



class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create_user(self, validate_data):
        email = validate_data['email']
        username = validate_data['username']
        first_name = validate_data['first_name']
        last_name = validate_data['last_name']
        password = validate_data['password']

        user = get_user_model()
        new_user = user.objects.create(email=email, username=username, first_name=first_name, last_name=last_name)
        new_user.set_password(password)
        new_user.save()

        return new_user


