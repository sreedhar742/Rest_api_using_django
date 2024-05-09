from django.shortcuts import render
# Create your views here.
from rest_framework import viewsets
from .models import Store
from .serializers import Storeser


class Storeview(viewsets.ModelViewSet):
    queryset=Store.objects.all()
    serializer_class=Storeser
from django.db import connection

def your_view(request):
    # Your existing view logic

    print(connection.queries)
