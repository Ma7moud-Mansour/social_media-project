from django.urls import path
from .views import PostListCreateView, CommentListCreateView
from . import views
from django.urls import path
from .views import CustomLoginView

urlpatterns = [
    #path('', PostListCreateView.as_view(), name='post-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('', views.Login, name = 'login'),
    path('postdetails', views.Post_details, name = 'post_details'),
    path('postlist', views.Post_list, name = 'post_list'),
    #path('signup', views.Signup, name = 'signup'),
    path('profileupdate', views.Profile_update, name = 'profile_update'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', views.Signup, name='signup'),
    path('postlist', views.Post_list, name='post_list'),
]
