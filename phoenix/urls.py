from django.urls import path

from . import views

urlpatterns = [
    path('name/<str:name>/', views.index, name='index'),
]