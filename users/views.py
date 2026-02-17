from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, ListView, TemplateView, UpdateView
from users.forms import UserRegisterForm, LoginForm, UpdateUserProfileForm, LoadingUserAvatarForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from main.models import SetupPosts
from users.models import BioUsers

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
            context['avatar_form'] = LoadingUserAvatarForm(instance=self.request.user.biousers)
            return context
    
    def get_queryset(self):
        user_id = self.kwargs['pk']
        
        sort = self.request.GET.get('status')
        if sort == 'my':
            return SetupPosts.objects.filter(creator_id=user_id).order_by('-time')
        elif sort == 'like':
            return SetupPosts.objects.filter(likes=user_id)

    def post(self, request, *args, **kwargs):
        form = LoadingUserAvatarForm(request.POST, request.FILES, instance=request.user.biousers)
        
        if form.is_valid():
            form.save()
            return redirect('users:profile', pk=request.user.pk)

        
    
class UpdateUserProfileView(LoginRequiredMixin, UpdateView):
    model = BioUsers
    form_class = UpdateUserProfileForm
    template_name = 'users/edit_user_profile.html'

    # Валидность 2-степень проверки на то есть ли у пользоваетля 10лайков профеля или нет 
    def form_valid(self, form):
        user = self.request.user
        total_likes = SetupPosts.objects.filter(creator = user).aggregate(all_likes_sum=Count('likes'))['all_likes_sum'] or 0

        if total_likes < 10 and 'background_image' in form.changed_data:
            form.cleaned_data.pop('background_image', None)
            return self.form_invalid(form)
        return super().form_valid(form)
    
    # который сейчас залогинен (request.user), и дай ему отредактировать только его собственную запись biousers
    def get_object(self, queryset=None):
        return self.request.user.biousers
    
    def get_success_url(self):
        return reverse('users:profile', kwargs={'pk': self.request.user.pk})
    









    
    