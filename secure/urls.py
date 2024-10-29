from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView
from myapp import views

urlpatterns = [
    path('', views.vulnerable, name='vulnerable'),
    path('secure/', views.secure, name='secure'),
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]