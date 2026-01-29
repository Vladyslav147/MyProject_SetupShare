from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateNewPostForm
from .models import SetupPosts
from django.urls import reverse_lazy
# Create your views here.
class MainPageViews(TemplateView):
    template_name = 'main/index.html'

class Add_NewPostView(LoginRequiredMixin, CreateView):
    model = SetupPosts
    template_name = 'main/add_post.html'
    form_class = CreateNewPostForm
    success_url = reverse_lazy('main:main_page')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)
    

