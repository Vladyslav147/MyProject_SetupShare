from django.urls import path
from main import views
app_name = 'main'

urlpatterns = [
    path('', views.MainPagePostViews.as_view(), name='main_page'),
    path('add_new_post/', views.Add_NewPostView.as_view(), name='add_post'),
    path('detail/<int:pk>', views.Detail_PostView.as_view(), name='detail_post'),
    path('deletpost/<int:pk>', views.Delet_PostView.as_view(), name='delet_post'),
    path('post-loke/<int:pk>', views.Post_likesView.as_view(), name='posts-likes'),
]
