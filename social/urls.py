from django.urls import path

from social import views

urlpatterns = [
    path('posts/', views.PostListCreateAPIView.as_view()),
]
