from django.urls import path

from user.api import views

urlpatterns = [
    path('profile/<str:username>/', views.ProfileRetrieveApiView.as_view()),
    path('profile/', views.ProfileRetrieveUpdateApiView.as_view()),
    path('profile-list/', views.ProfileListAPIView.as_view())
]
