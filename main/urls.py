from django.urls import path
from main import views
app_name = 'main'

urlpatterns = [
    path('', views.MainPageViews.as_view(), name='main_page'),
    path('add_new_post/', views.Add_NewPostView.as_view(), name='add_post'),
]
