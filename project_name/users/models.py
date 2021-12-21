from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """User"""
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone']

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    email = models.EmailField(verbose_name=_('email address'), unique=True)
    phone = models.CharField(verbose_name=_('phone'), max_length=15, unique=True)
