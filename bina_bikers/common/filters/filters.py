import django_filters

from bina_bikers.pg_search.filters import SearchFilter


class BaseFilterSet(django_filters.FilterSet):
    search = SearchFilter()
