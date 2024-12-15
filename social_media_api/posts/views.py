from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.filters import Comment.objects.all()
from rest_framework.filters import Post.objects.filter(author__in=following_users).order_by 
from rest_framework.filters import generics.get_object_or_404(Post, pk=pk)
from rest_framework.filters import Like.objects.get_or_create(user=request.user, post=post)
from rest_framework.filters import following.all()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
# posts/views.py
from rest_framework import status, permissions, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Post, Like
from notifications.models import Notification
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    # Like a post
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Fetch the post by pk
        user = request.user
        
        # Handle creating or retrieving the like instance
        like, created = Like.objects.get_or_create(user=user, post=post)
        
        # If the like was already created, we can return an error message
        if not created:
            return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a notification for the post author
        notification = Notification.objects.create(
            recipient=post.author,
            actor=user,
            verb="liked",
            target=post,
            target_content_type=ContentType.objects.get_for_model(Post),
        )
        
        return Response({"message": "Post liked."}, status=status.HTTP_200_OK)

    # Unlike a post
    @action(detail=True, methods=['post'])
    def unlike(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)  # Fetch the post by pk
        user = request.user
        
        # Check if the user has liked the post
        try:
            like = Like.objects.get(user=user, post=post)
            like.delete()  # Delete the like
            return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)
        except Like.DoesNotExist:
            return Response({"error": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
