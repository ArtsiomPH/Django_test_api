from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from .paginators import PageNumberSizePaginator

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    pagination_class = PageNumberSizePaginator
