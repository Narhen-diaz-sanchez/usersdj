from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import (
    TemplateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import *
# Create your views here.

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'home/index.html'
    login_url = reverse_lazy('users_app:user-login')

class HomeView(TemplateView):
    template_name='home/index.html'
    
    
