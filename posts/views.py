from rest_framework import generics 
from rest_framework.permissions import IsAuthenticated 
from rest_framework import views 
from rest_framework.response import Response
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect


class CustomLoginView(LoginView):
    template_name = 'pages/login.html'
    success_url = reverse_lazy('post_list')  # Redirect to post list after login

@csrf_protect
def Signup(request):
    if request.method == 'POST':
        # Assuming you're processing the form here
        # After successful signup
        return redirect('post_list.html')  # Redirect to post list after signup
    return render(request, 'pages/signup.html')

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')
        content = self.request.query_params.get('content', None)
        
        if content:
            queryset = queryset.filter(content__icontains=content)
        
        return queryset

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserPostsView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Post.objects.filter(user_id=user_id)


def Login(request):
    return render(request, 'pages/login.html')
    

def Post_details(request):
    return render(request, 'pages/post_details.html')

#def Signup(request):
    return render(request, 'pages/signup.html')

def Post_list(request):
    return render(request, 'pages/post_list.html')

def Profile_update(request):
    return render(request, 'pages/profile_update.html')
