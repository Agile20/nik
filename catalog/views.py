from rest_framework import generics, viewsets 

from .models import *
from .serializers import *


class CatalogCarView(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CatalogCarSerializer


class CatalogBikeView(viewsets.ModelViewSet):
    queryset = Bike.objects.all()
    serializer_class = CatalogBikeSerializer


class CatalogOtherTransportView(viewsets.ModelViewSet):
    queryset = OtherTransport.objects.all()
    serializer_class = CatalogOtherTransportSerializer



