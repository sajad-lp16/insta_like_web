from django.contrib.auth import get_user_model
from django.db import transaction
from django.shortcuts import redirect, get_object_or_404
from django.views import generic
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from relation.models import Relation
from relation.serializers import RelationSerializer

User = get_user_model()


class FollowView(generic.FormView):
    def post(self, request, *args, **kwargs):
        from_user = self.request.user
        username = self.request.POST.get('username')
        to_user = get_object_or_404(User, username=username)
        if not from_user == to_user:
            with transaction.atomic():
                relation = Relation.objects.filter(from_user=from_user, to_user=to_user)
                if relation.exists():
                    relation[0].delete()
                else:
                    Relation.objects.create(from_user=from_user, to_user=to_user)
        return redirect('profile/{}'.format(username))


class FollowersListApiView(generics.ListAPIView):
    queryset = Relation.objects.select_related('from_user').all()
    serializer_class = RelationSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(to_user=self.request.user)
