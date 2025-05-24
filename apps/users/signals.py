from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import UserProfile, UserPreference

@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=UserProfile)
def create_user_preferences(sender, instance, created, **kwargs):
    if created and not instance.preferences:
        preferences = UserPreference.objects.create(user=instance.user)
        instance.preferences = preferences
        instance.save()

