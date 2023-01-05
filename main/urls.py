from django.urls import path
from main.views import *

urlpatterns = [
    path('mainpicture/', MainPictureView.as_view()),
    path('maincatalog/', MainCatalogView.as_view()),
    path('aboutus/', MainAboutUsView.as_view()),
    path('connection/', MainConnectionView.as_view()),
]