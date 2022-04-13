from django.urls import path

from posts.views import PostsListView, PostsDetailView

app_name = 'posts'

urlpatterns = [
    path('', PostsListView.as_view(), name="list"),
    path('<int:pk>/', PostsDetailView.as_view(), name="detail"),
]