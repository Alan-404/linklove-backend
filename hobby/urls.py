from django.urls import path
from hobby import views
urlpatterns = [
    path('hobby_api', views.hobby_api)
]