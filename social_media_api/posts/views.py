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
