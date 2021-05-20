from django.urls import path

from activity import views

urlpatterns = [
    path('comments/', views.CommentCreateAPIView.as_view(), name='comments'),
]
