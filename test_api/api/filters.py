from django_filters.rest_framework import FilterSet, NumberFilter
from .models import User


class NumParamsFilter(FilterSet):
    min_age = NumberFilter(field_name="age", lookup_expr='gte')
    max_age = NumberFilter(field_name="age", lookup_expr='lte')

    min_weight = NumberFilter(field_name="weight", lookup_expr='gte')
    max_weight = NumberFilter(field_name="weight", lookup_expr='lte')

    class Meta:
        model = User
        fields = '__all__'
