from django.urls import path
from . import views

urlpatterns = [
    path('', views.score1.as_view(), name='score1'),
]