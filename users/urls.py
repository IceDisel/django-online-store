from django.contrib.auth.views import LoginView, LogoutView, PasswordResetConfirmView
from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, ConfirmRegistrationUserView, CustomPasswordResetView


app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('confirm/', ConfirmRegistrationUserView.as_view(), name='confirm'),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset/', CustomPasswordResetView.as_view(), name='reset'),
    path('reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
