from django.core.validators import FileExtensionValidator
from django.db import models
from lib.common_models import BaseModel
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from location.models import Location

User = get_user_model()


class Post(BaseModel):
    user = models.ForeignKey(User, related_name="posts",
                             on_delete=models.CASCADE)
    caption = models.TextField(_('caption'), blank=True)
    location = models.ForeignKey(
        Location, related_name="posts", on_delete=models.CASCADE, blank=True)

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def __str__(self):
        return str(self.user)


class Media(BaseModel):
    IMAGE = 1
    VIDEO = 2
    CHOICES = (
        (IMAGE, _('image')),
        (VIDEO, _('video')),
    )
    post = models.ForeignKey(Post, related_name="media",
                             on_delete=models.CASCADE)
    file = models.FileField(_('file'),
                            upload_to='posts/Y-m/',
                            validators=[FileExtensionValidator(
                                allowed_extensions=['jpg', 'jpeg', 'mp4', 'flv', 'mkv'])])

    class Meta:
        verbose_name = _('media')
        verbose_name_plural = _('media')

    def __str__(self):
        return "{}".format(str(self.post))


class Tag(BaseModel):
    title = models.CharField(_('title'), max_length=32)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


class PostTag(BaseModel):
    post = models.ForeignKey(Post, related_name="tags",
                             on_delete=models.CASCADE)
    tag = models.ForeignKey(
        Tag, related_name="post_tags", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('post_tag')
        verbose_name_plural = _('post_tags')

    def __str__(self):
        return str(self.post)


class UserTag(BaseModel):
    user = models.ForeignKey(User, related_name="tags",
                             on_delete=models.CASCADE)
    tag = models.ForeignKey(
        Tag, related_name="user_tags", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('user_tag')
        verbose_name_plural = _('user_tags')

    def __str__(self):
        return str(self.user)
