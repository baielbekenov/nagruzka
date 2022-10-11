import django_filters

from nagr.models import Teacher


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Teacher
        fields = ['name']