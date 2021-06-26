from django.db import models
from lib.common_models import BaseModel
from django.contrib.auth import get_user_model
from social.models import Post
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class Comment(BaseModel):
    user     = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    post     = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content  = models.TextField(_('comment'))
    caption  = models.TextField(_('caption'))
    reply_to = models.ForeignKey(
        'self', blank=True, null=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        verbose_name        = _('comment')
        verbose_name_plural = _('comments')

    def __str__(self):
        return "{} on {}".format(str(self.user), str(self.post))


class Like(BaseModel):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)

    class Meta:
        verbose_name        = _('like')
        verbose_name_plural = _('likes')

    def __str__(self):
        return "{} on {}".format(str(self.user), str(self.post))
