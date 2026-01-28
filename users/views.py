from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView
from users.forms import UserRegisterForm, LoginForm
from django.contrib.auth import login, logout
# Create your views here.

class PageLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = LoginForm

    def form_valid(self, form):
        return super().form_valid(form)

class LogoutUser(LogoutView):
    pass
    
class PageRegistersView(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy('main:main_page'))
    
    
    