from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, TemplateView
from users.forms import UserRegisterForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from main.models import SetupPosts
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
    
class UserProfileView(LoginRequiredMixin, ListView):
    template_name = 'users/user_profile.html'
    model = SetupPosts
    context_object_name = 'post'

    def get_queryset(self):
        sort = self.request.GET.get('status')
        if sort == 'my':
            return SetupPosts.objects.filter(creator_id=self.kwargs['pk']).order_by('-time')
        elif sort == 'like':
            return SetupPosts.objects.filter(likes=self.kwargs['pk'])

    
    

    









    
    