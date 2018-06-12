from django.urls import path
from . import views

app_name = 'gestionOT'
urlpatterns = [
    path('', views.index, name='index'),
]
