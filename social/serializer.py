from rest_framework import serializers

from location.serializer import LocationSerializer
from social.models import Post, Media
from user.api.serializers import UserSerializer


class PostMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Media
        fields = ('file',)


class PostSerializer(serializers.ModelSerializer):
    user     = UserSerializer()
    location = LocationSerializer()
    media    = PostMediaSerializer(many=True)

    class Meta:
        model  = Post
        fields = ('user', 'created_time', 'caption', 'location', 'media')
