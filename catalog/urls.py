from django.urls import path
from .views import *

urlpatterns = [
    path('car/', CatalogCarView.as_view({'get': 'list'})),
    path('bike/', CatalogBikeView.as_view({'get': 'list'})),
    path('othertrsnsport/', CatalogOtherTransportView.as_view({'get': 'list'})),
]