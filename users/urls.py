from django.urls import path
from .views import SignupView, CustomTokenObtainPairView, UserListView, UserProfileView
from posts.views import UserPostsView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('search/', UserListView.as_view(), name='user-list'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('profile/<int:user_id>/posts/', UserPostsView.as_view(), name='user-posts'),
]
