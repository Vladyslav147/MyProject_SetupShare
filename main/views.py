from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateNewPostForm
from .models import SetupPosts
from django.urls import reverse_lazy
# Create your views here.

class MainPagePostViews(ListView):
    template_name = 'main/index.html'
    model = SetupPosts
    context_object_name = 'posts'
    ordering = ['-time'] # Сортировка по времени публикации поста, time это поле из модели

    def get_queryset(self):
        sort = self.request.GET.get('status')
        if sort == 'old':
            return SetupPosts.objects.order_by('time')
        elif sort == 'new':
            return SetupPosts.objects.order_by('-time')
        else:
            return SetupPosts.objects.all().order_by('-time')
        

class Add_NewPostView(LoginRequiredMixin, CreateView):
    model = SetupPosts
    template_name = 'main/add_post.html'
    form_class = CreateNewPostForm
    success_url = reverse_lazy('main:main_page')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    
class Detail_PostView(LoginRequiredMixin, DetailView):
    template_name  = 'main/detail_post.html'
    model = SetupPosts
    context_object_name = 'DetailPost'
    
class Delet_PostView(LoginRequiredMixin, DeleteView):
    model = SetupPosts
    success_url = reverse_lazy('main:main_page')

