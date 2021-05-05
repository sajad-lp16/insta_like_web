from django.db import models
from lib.common_models import BaseModel
from django.utils.translation import ugettext_lazy as _


class Location(BaseModel):
    title = models.CharField(max_length=32)
    points = models.JSONField(_('points'))

    def __str__(self):
        return self.title
