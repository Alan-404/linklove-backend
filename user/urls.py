from django.urls import path
from user import views

urlpatterns = [
    path('user_api',views.user_api ),
    path('auth', views.auth_user),
    path('info', views.info_user)
]