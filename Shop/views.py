from django.shortcuts import render,redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, View
from django.views.generic import CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from .forms import AnnouncementForms, PhotoFormSet
from .models import Announcement, PhotoAnnouncement
from django.contrib import messages
from Shop import models
from users.models import CustomRegisterUser
from django.db.models import Q
# Create your views here.
from django.http import JsonResponse
class ShopPageView(LoginRequiredMixin, ListView):
    template_name = 'shop/index_shop.html'
    context_object_name = 'Announcement'
    model = Announcement
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        sort = self.request.GET.get('status')

        if query:
            return Announcement.objects.filter(Q(title__icontains=query)| Q(description__icontains=query))

        if sort == 'price_asc':
            return Announcement.objects.order_by('price')
        elif sort == 'price_desc':
            return Announcement.objects.order_by('-price')
        elif sort == 'newest':
            return Announcement.objects.all()
        elif sort == 'spareparts':
            return Announcement.objects.filter(state='spareparts')
        elif sort == 'new':
            return Announcement.objects.filter(state='new')
        elif sort == 'average':
            return Announcement.objects.filter(state='average')
        else:
            return Announcement.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get('q')
        return context
    


class AddProductView(LoginRequiredMixin, CreateView):
    form_class = AnnouncementForms
    success_url = reverse_lazy('Shop:mainshop')
    template_name = 'shop/add_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "Photo_form" not in context:
            context["Photo_form"] = PhotoFormSet() 
        return context

    def post(self, request, *args, **kwargs):
        self.object = None # то что ссылка может уже создаватся для записи с уникальным id но быть пустой пока-что, (ссылка это строка из таблицы с уникальным id)

        form_class = self.get_form_class() # с какой формой будем работать
        form = self.get_form(form_class) # достаем из нее данные 
        Photo_form = PhotoFormSet(self.request.POST, self.request.FILES)

        if form.is_valid() and Photo_form.is_valid():
            return self.form_valid(form, Photo_form)
        else:
            return self.form_invalid(form, Photo_form)

    def form_valid(self, form, Photo_form):
        form.instance.creator = self.request.user
        self.object = form.save()
        Photo_form.instance = self.object
        Photo_form.save()
        
        return redirect(self.get_success_url())

    
class DetailProductView(LoginRequiredMixin, DetailView):
    template_name = 'shop/detail_product.html'
    model = Announcement
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        context["photo"] = PhotoAnnouncement.objects.filter(announcement_id=pk)
        return context
    

class ShopUserProfileView(LoginRequiredMixin, ListView):
    template_name = 'shop/shop_profile.html'
    model = Announcement
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get('pk')

        context['profile'] = get_object_or_404(CustomRegisterUser, pk=user_id)
        context["all_post"] = Announcement.objects.filter(creator_id=user_id).count
        return context
    
    def get_queryset(self):
        user_id = self.kwargs['pk']
        status = self.request.GET.get('status')
        if status == 'my':
            return Announcement.objects.filter(creator_id=user_id)
        elif status == 'likes':
            return Announcement.objects.filter(likes = user_id)

class ShopDeletView(LoginRequiredMixin, DeleteView):
    model = Announcement
    success_url = reverse_lazy('Shop:mainshop')
    
    def get_queryset(self):
        return Announcement.objects.filter(creator_id=self.request.user)
    
class LikeProductView(LoginRequiredMixin, View):
    def post(self, request, pk):
        product_id = get_object_or_404(models.Announcement, pk=pk)
        if request.user in product_id.likes.all():
            product_id.likes.remove(request.user)
            like = False
        else:
            product_id.likes.add(request.user)
            like = True

        return JsonResponse({
            'liked': like
        })