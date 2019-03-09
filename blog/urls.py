from django.urls import path
from . import views
from .views import search, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView, ReviewCreateView, ReviewListView, ReviewDetailView, ReviewDeleteView, ReviewUpdateView, ReviewLastView

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('search/', views.search, name = 'search-func'),
    path('user/<str:username>/', UserPostListView.as_view(), name = 'user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('about/', views.about, name = 'blog-about'),
    path('review/new/', ReviewCreateView.as_view(), name = 'review-create'),
    path('reviews/', ReviewListView.as_view(), name = 'review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name = 'review-detail'),
    path('reviews/<int:pk>/delete/', ReviewDeleteView.as_view(), name = 'review-delete'),
    path('reviews/<int:pk>/update/', ReviewUpdateView.as_view(), name = 'review-update'),
    path('reviews-last/', ReviewLastView.as_view(), name = 'review-last'),
]