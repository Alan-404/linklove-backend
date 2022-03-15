from django.urls import path
from post import views
urlpatterns = [
    path('post_api', views.post_api),
    path('user', views.posts_user),
    path('add_post', views.post),
    path('all', views.get_posts)
]