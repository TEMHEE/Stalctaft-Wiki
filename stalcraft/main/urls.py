from django.urls import path
from  . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('maps', views.maps),
    path('pvp', views.pvp),
    path('artifacts', views.artifacts),
    path('guides', views.guides),
    path('login', views.login),
]
