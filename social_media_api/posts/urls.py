from django.urls import path
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('feed/', feed.as_view(), name='feed'),
    path('<int:pk>/like/', feed.as_view(), name='feed'),
    path('<int:pk>/unlike/', feed.as_view(), name='feed'),
]
