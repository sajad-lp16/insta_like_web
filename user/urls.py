from django.urls import path, re_path
from . import views

app_name = 'user'

urlpatterns = [
    path('register/', views.RegisterView.as_view(),                    name='auth-register'),
    path('login/', views.LoginView.as_view(),                          name='auth-login'),
    path('update_profile/', views.ProfileUpdateView.as_view(),         name='update-profile'),
    path('profile/<str:username>/', views.ProfileDetailView.as_view(), name='profile'),
]
