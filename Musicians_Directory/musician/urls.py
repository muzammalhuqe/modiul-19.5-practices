from django.urls import path, include
from . import views
urlpatterns = [
    # path('add/', views.add_musician, name = 'add_musician'),
    path('add/', views.AddMusicianCreateView.as_view(), name = 'add_musician'),
    path('singup/', views.user_singup, name = 'singup'),
    # path('singup/', views.SignUpView.as_view(), name = 'singup'),
    # path('login/', views.user_login, name = 'login'),
    path('login/', views.UserLoginView.as_view(), name = 'login'),
    # path('logout/', views.user_logout, name = 'logout'),
    path('logout/', views.UserLogoutView.as_view(), name = 'logout'),
    path('profile/', views.user_profile, name = 'profile'),
]