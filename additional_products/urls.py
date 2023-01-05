from django.urls import path
from .views import *

urlpatterns = [
    path('spareparts/', SparePartsView.as_view({'get': 'list'})),
    path('car/', PowerPlantView.as_view({'get': 'list'})),
]