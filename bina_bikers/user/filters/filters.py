import django_filters

import bina_bikers.user.models as models
from bina_bikers.common.filters import BaseFilterSet


class UserFilter(BaseFilterSet):
    user_type = django_filters.CharFilter(name='user_type')

    class Meta:
        model = models.User
        fields = (
            'first_name', 'last_name', 'email',
            'phone_number', 'user_type')


class UserProfileFilter(BaseFilterSet):

    class Meta:
        model = models.UserProfile
        fields = ('id',)
