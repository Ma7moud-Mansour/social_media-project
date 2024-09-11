from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.name')
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'created_at', 'comments']
