from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from user.api.serializers import UserSerializer, UserLightSerializer

User = get_user_model()


class ProfileRetrieveApiView(generics.RetrieveAPIView):
    queryset         = User.objects.all()
    lookup_url_kwarg = 'username'
    lookup_field     = 'username'
    serializer_class = UserSerializer


class ProfileRetrieveUpdateApiView(generics.RetrieveUpdateAPIView):
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes     = (IsAuthenticated,)
    serializer_class       = UserSerializer

    def get_object(self):
        return self.request.user


class ProfileListAPIView(generics.ListCreateAPIView):
    queryset               = User.objects.all()
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes     = (IsAuthenticated,)
    serializer_class       = UserSerializer
