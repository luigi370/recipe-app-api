from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Tag
from . import serializer


# Create your views here.
class TagViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = serializer.TagSerializer

    def get_queryset(self):
        """Return object for the current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')
