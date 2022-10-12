from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format="%d-%m-%Y")

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'country', 'birth_date', 'age', 'weight']
