from django.db.models import Model, CharField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class Car(Model):
    model = CharField(_("Model"), blank=True, max_length=255)

    class Meta:
        verbose_name = _("Car")
        verbose_name_plural = _("s")

    def __str__(self):
        return self.model

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
