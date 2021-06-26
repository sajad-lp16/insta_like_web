from django.db import models
from django.contrib.auth import get_user_model
from lib.common_models import BaseModel
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Relation(BaseModel):
    from_user = models.ForeignKey(User, related_name='followings', on_delete=models.CASCADE)
    to_user   = models.ForeignKey(User,  related_name='followers', on_delete=models.CASCADE)

    class Meta:
        verbose_name        = _('relation')
        verbose_name_plural = _('relations')

    def __str__(self):
        return "({follower}) >>> ({following})".format(
            follower =self.from_user.username,
            following=self.to_user.username,
        )
