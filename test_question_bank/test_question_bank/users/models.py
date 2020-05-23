from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(verbose_name=_("Name of User"), blank=True, max_length=255)
    mobile = models.CharField(verbose_name=_('Mobile phone number'), blank=True, max_length=16, unique=True)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    class Meta:
        db_table = 'User'
        verbose_name = _('User Info')
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
