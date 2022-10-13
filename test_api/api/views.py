import django_filters
from rest_framework import viewsets, filters, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .serializers import UserSerializer
from .models import User
from .paginators import PageNumberSizePaginator
from .filters import NumParamsFilter


class UserViewSet(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = PageNumberSizePaginator
    filter_backends = [filters.SearchFilter, django_filters.rest_framework.DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = NumParamsFilter
    search_fields = ['first_name', 'last_name', 'country']




