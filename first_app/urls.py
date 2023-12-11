from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', views.userlogin, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.userlogout, name='logout'),
    path('pass_change/', views.passward_change, name='passwordChange'),
    path('pass_change2/', views.passward_change2, name='passwordChange2'),
]
