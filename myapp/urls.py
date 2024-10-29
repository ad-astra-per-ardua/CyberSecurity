from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vulnerable', views.vulnerable, name="vulnerable"),
    path('secure',views.secure, name="secure"),
]