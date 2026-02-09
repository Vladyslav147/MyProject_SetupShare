from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from main import models
from django.views.generic import CreateView, DeleteView, DetailView, View, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateNewPostForm, UpdatePostForm
from .models import SetupPosts
from django.urls import reverse_lazy, reverse
from django.db.models import Count
from django.core.paginator import Paginator
# Create your views here.

class MainPagePostViews(ListView):
    template_name = 'main/index.html'
    model = SetupPosts
    context_object_name = 'posts'
    ordering = ['-time'] # Сортировка по времени публикации поста, time это поле из модели
    paginate_by = 12

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


class Post_likesView(LoginRequiredMixin, View):
    def post(self, request, pk):
        posts = get_object_or_404(models.SetupPosts, pk=pk)

        if request.user in posts.likes.all():
            posts.likes.remove(request.user)
        else:
            posts.likes.add(request.user)

        return redirect('main:detail_post', pk=pk)
    

class UpdatePostView(LoginRequiredMixin, UpdateView):
    model = SetupPosts
    form_class = UpdatePostForm
    template_name = 'main/edit_post.html'
    
    def get_success_url(self):
        return reverse('main:detail_post', kwargs={'pk': self.object.pk})

    

