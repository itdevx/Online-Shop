from django.urls import path
from account.views import *


app_name = 'account'

urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('forgot', ForgotView.as_view(), name='forgot'),
    path('logout', LogoutRequest.as_view(), name='logout'),
]