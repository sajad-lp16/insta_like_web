from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    created_time = models.DateTimeField(_('created time'), auto_now_add=True)
    modeified_time = models.DateTimeField(_('modeified time'), auto_now=True)

    class Meta:
        abstract = True
