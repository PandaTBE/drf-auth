from django.db import models
from django.contrib.auth.models import AbstractUser
from users.managers import UserManager
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(verbose_name=_("Email address"), unique=True)
    first_name = models.CharField(verbose_name=_("Name"), max_length=64)
    last_name = models.CharField(
        verbose_name=_("Last name"), max_length=64, null=True, blank=True
    )
    second_name = models.CharField(
        verbose_name=_("Second name"), max_length=64, null=True, blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name"]

    objects = UserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    location = models.CharField(max_length=256, blank=True, null=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
