from rest_framework import serializers
from .models import Store

class Storeser(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Store
        fields='__all__'
        