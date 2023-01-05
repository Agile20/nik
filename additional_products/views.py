from rest_framework import generics, viewsets 

from .models import *
from .serializers import *


class SparePartsView(viewsets.ModelViewSet):
    queryset = SpareParts.objects.all()
    serializer_class = SparePartsSerializer


class PowerPlantView(viewsets.ModelViewSet):
    queryset = PowerPlant.objects.all()
    serializer_class = PowerPlantSerializer