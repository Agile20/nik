from rest_framework import generics, viewsets 

from .models import *
from .serializers import *


class MainPictureView(generics.CreateAPIView):
    queryset = MainPicture.objects.all() 
    serializer_class = MainPictureSerializer


class MainCatalogView(generics.CreateAPIView):
    queryset = MainCatalog.objects.all() 
    serializer_class = MainCatalogSerializer


class MainAboutUsView(generics.CreateAPIView):
    queryset = AboutUs.objects.all() 
    serializer_class = MainAboutUsSerializer


class MainConnectionView(generics.CreateAPIView):
    queryset = Connection.objects.all() 
    serializer_class = MainConnectionSerializer

