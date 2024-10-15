from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/myapp/', permanent=True)),
    path('myapp/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]