from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, TemplateView
from users.forms import UserRegisterForm, LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from main.models import SetupPosts
from django.db.models import Count
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


    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user_id = self.kwargs.get('pk')

            total_likes = SetupPosts.objects.filter(creator_id=user_id).aggregate(all_likes_sum=Count('likes'))['all_likes_sum']
            all_post_user = SetupPosts.objects.filter(creator_id = user_id).count()
            
            context['total_likes'] = total_likes or 0
            context['all_post'] = all_post_user or 0
            return context
    
    def get_queryset(self):
        user_id = self.kwargs['pk']
        
        sort = self.request.GET.get('status')
        if sort == 'my':
            return SetupPosts.objects.filter(creator_id=user_id).order_by('-time')
        elif sort == 'like':
            return SetupPosts.objects.filter(likes=user_id)

    
    

    









    
    