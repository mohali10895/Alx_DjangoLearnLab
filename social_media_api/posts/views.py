from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.filters import Comment.objects.all()
from rest_framework.filters import Post.objects.filter(author__in=following_users).order_by 
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
from django.contrib.auth import get_user_model
from .models import Post, Like
from notifications.models import Notification
from django.contrib.contenttypes.models import ContentType

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    
    # Like a post
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        
        # Check if user has already liked the post
        if Like.objects.filter(user=user, post=post).exists():
            return Response({"error": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        like = Like.objects.create(user=user, post=post)
        
        # Create notification for the post author
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
        post = self.get_object()
        user = request.user
        
        # Check if user has liked the post
        like = Like.objects.filter(user=user, post=post).first()
        if not like:
            return Response({"error": "You have not liked this post."}, status=status.HTTP_400_BAD_REQUEST)
        
        like.delete()
        
        # Optionally, remove notification (if necessary)
        return Response({"message": "Post unliked."}, status=status.HTTP_200_OK)
