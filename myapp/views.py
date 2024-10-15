from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import score1

class score1(ListView):
    model = score1
    template_name = 'index.html'


