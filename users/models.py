from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):

    bio = models.TextField(blank=True, null=True)
    photo_user = models.ImageField(upload_to="users/photo/profile/", blank=True)

    def __str__(self):
        return str(self.username)



