from django.shortcuts import render
from django.views.generic import CreateView
from .forms import RegisterForm


# Create your views here.
class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/'