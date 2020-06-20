from django.urls import path,include
from . import views
import djoser
urlpatterns = [
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken'))
]