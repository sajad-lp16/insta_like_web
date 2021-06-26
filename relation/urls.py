from django.urls import path

from relation import views

app_name = 'relation'

urlpatterns = [
    path('follow-unfollow', views.FollowView.as_view(),      name='follow-unfollow'),
    path('followers/', views.FollowersListApiView.as_view(), name='followers'),
]
