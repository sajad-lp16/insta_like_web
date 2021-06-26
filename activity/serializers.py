from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from django.utils.translation import ugettext_lazy as _

from activity.models import Comment
from social.serializer import PostSerializer
from user.api.serializers import UserLightSerializer


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Comment
        fields = ('post', 'caption', 'reply_to')

    def validate(self, attrs):
        if attrs['reply_to'] is not None and attrs['reply_to'].post != attrs['post']:
            raise ValidationError(_('comment and reply are not related to the same post'))
        return attrs
