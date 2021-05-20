from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from django.contrib.auth import get_user_model
from social.models import Post

from social.serializer import PostSerializer
from rest_framework import generics

from user.api.serializers import UserSerializer

User = get_user_model()


class PostListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(user=self.request.user)

