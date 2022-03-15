from django.urls import path
from friend_request import views
urlpatterns = [
    path('request_api', views.friend_request_api),
    path('auth', views.request_handle)
]