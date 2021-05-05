from django.db import models
from lib.common_models import BaseModel
from django.utils.translation import ugettext_lazy
from django.contrib.auth import get_user_model
from location.models import Location

User = get_user_model()


class Post(BaseModel):
    user = models.ForeignKey(User, related_name="posts",
                             on_delete=models.CASCADE)
    caption = models.TextField(_('caption'), blank=True)
    location = models.ForeignKey(
        _('location'), related_name="posts", on_delete=models.CASCADE, blank=True)

    class class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return self.user


class Media(BaseModel):
    IMAGE = 1
    VIDEO = 2
    CHOICES = (
        (IMAGE, _('image')),
        (VIDEO, _('video')),
    )
    post = models.ForeignKey(Post, related_name="media",
                             on_delete=models.CASCADE)
    file = models.FileField(_('file'), upload_to='/posts/Y-m/')

    def __str__(self):
        return "{}  -  {}".format(str(self.post), self.get_media_type_display())


class Tag(BaseModel):
    title = models.CharField(_('title'), max_length=32)

    def __str__(self):
        return self.title


class PostTag(BaseModel):
    post = models.ForeignKey(Post, related_name="tags",
                             on_delete=models.CASCADE)
    tag = models.ForeignKey(
        Tag, related_name="post_tags", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.post)


class UserTag(BaseModel):
    user = models.ForeignKey(User, related_name="tags",
                             on_delete=models.CASCADE)
    tag = models.ForeignKey(
        Tag, related_name="user_tags", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
