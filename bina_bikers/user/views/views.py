from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.permissions import AllowAny

import bina_bikers.user.filters as filters
import bina_bikers.user.serializers as serializers
import bina_bikers.user.models as models


class UserViewSet(ModelViewSet):
    """
    This is the user's endpoint. It contains the details that are stored for
    a user using our system.
    """
    permission_classes = (AllowAny, )
    queryset = models.User.objects.all()
    filter_class = filters.UserFilter
    serializer_class = serializers.UserSerializer
    search_fields = ('first_name', 'last_name', 'email')


class UserProfileViewSet(ModelViewSet):
    """
    This provides a way to add extra details to our users. It has a OneToOne
    relationship with the User model that is provided by django.
    """
    queryset = models.UserProfile.objects.all()
    filter_class = filters.UserProfileFilter
    serializer_class = serializers.UserProfileSerializer


class MeView(generics.RetrieveUpdateDestroyAPIView):
    """
    This view is user to get the details of a logged in user.
    """
    queryset = None
    serializer_class = serializers.UserSerializer

    def get_object(self):
        return self.request.user
