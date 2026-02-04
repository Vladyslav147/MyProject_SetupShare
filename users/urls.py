from django.urls import path
from users import views
app_name = 'users'

urlpatterns = [
    path('login/', views.PageLoginView.as_view(), name='login'),
    path('register/', views.PageRegistersView.as_view(), name='registers'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('user_profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
]
