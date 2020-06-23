from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, Model
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Plane(Model):
    name = CharField(_("Name of plane"), blank=True, max_length=255)

    class Meta:
        verbose_name = _("Plane")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
