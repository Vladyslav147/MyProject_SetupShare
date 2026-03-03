from django.urls import path
from Shop import views
app_name = 'Shop'

urlpatterns = [
    path('', views.ShopPageView.as_view(), name='mainshop'),
    path('add_product/', views.AddProductView.as_view(), name='add-product'),
    path('detail_product/<int:pk>/', views.DetailProductView.as_view(), name='detail-product'),
    path('profile/<int:pk>/', views.ShopUserProfileView.as_view(), name='shop-profile'),
    path('delet_product/<int:pk>/', views.ShopDeletView.as_view(), name='delet_product'),
    path('like_product/<int:pk>/', views.LikeProductView.as_view(), name='like-product'),
]
