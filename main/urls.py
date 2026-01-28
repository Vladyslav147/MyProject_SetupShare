from django.urls import path
from main import views
app_name = 'main'

urlpatterns = [
    path('', views.MainPageViews.as_view(), name='main_page'),
]
