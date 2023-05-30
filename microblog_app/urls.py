from django.urls import path
from .views import UserCreateView, UserLoginView, PostCreateView, PostListView

urlpatterns = [
    path('users/register/', UserCreateView.as_view(), name='user-create'),
    path('users/login/', UserLoginView.as_view(), name='user-login'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/feed/', PostListView.as_view(), name='post-list'),
]
