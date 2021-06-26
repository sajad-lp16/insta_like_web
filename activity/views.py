from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from activity.models import Comment
from activity.serializers import CommentSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    permission_classes     = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class       = CommentSerializer
    queryset               = Comment.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
