from rest_framework import serializers

from user.api.serializers import UserLightSerializer
from .models import Relation


class RelationSerializer(serializers.ModelSerializer):
    from_user    = UserLightSerializer()
    is_following = serializers.SerializerMethodField()

    class Meta:
        model  = Relation
        fields = ('from_user', 'created_time', 'is_following')

    def get_is_following(self, obj):
        return Relation.objects.filter(from_user=obj.to_user, to_user=obj.from_user).exists()
