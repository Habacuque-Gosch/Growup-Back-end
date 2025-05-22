from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime




class CustomUser(AbstractUser):
    USER_TYPES = (
        ('blogger', 'blogger'),
        ('usuario', 'Usuário'),
    )
    type_user = models.CharField(max_length=10, choices=USER_TYPES)

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from apps.courses.models import Course
from django.conf import settings

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = get_user_model().objects.get(email=username)
            if user.check_password(password):
                return user
        except get_user_model().DoesNotExist:
            return None

class UserPreference(models.Model):
    receive_email = models.BooleanField(default=True)
    # receive_push = models.BooleanField(default=True)
    receive_news = models.BooleanField(default=True)
    receive_mesage = models.BooleanField(default=True)
    receive_promo = models.BooleanField(default=False)

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='preferences', null=True)

    def __str__(self):
        return str(self.user.username)

class UserProfile(models.Model):
    sex_orientation = [
        ('LESBICA','Lésbica'),
        ('GAY','Gay'),
        ('BISSEXUAL','Bissexual'),
        ('TRANSGENERO','Transgênero'),
        ('NAO_BINARIO','Não-Binário'),
        ('HETEROSSEXUAL','Heterossexual'),
        ('OUTRO','Outro'),
    ]

    name = models.CharField(max_length=150, null=False, blank=False)
    age = models.CharField(max_length=2, null=False, blank=False)
    bio = models.CharField(max_length=500, null=True, blank=True)
    sexual_orientation = models.CharField(max_length=100, choices=sex_orientation, default='')
    photo = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True, null=True)
    courses_save = models.ManyToManyField(Course, related_name='courses_save', blank=True)
    # friends = models.ManyToManyField(to=CustomUser, blank=True, related_name="friends")
    preferences = models.OneToOneField(UserPreference, on_delete=models.CASCADE, related_name='user_preferences', null=True, blank=True)
    user = models.ForeignKey(
        to=CustomUser,
        on_delete=models.CASCADE,
        null=True,
        blank=False,
        related_name="user",
    )
    
    def __str__(self):
        return self.name

    def get_profile(user):
        profile = UserProfile.objects.get(user=user)
        return profile

