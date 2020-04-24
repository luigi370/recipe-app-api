from .serializers import UserSerializers
from rest_framework import generics


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    """Creates a new user in the system"""
    serializer_class = UserSerializers
