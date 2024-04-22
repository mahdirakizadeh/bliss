from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.UserSignupView.as_view(), name='user_sign_up'),
    path('verify/', views.UserSignupVerifyView.as_view(), name='verify_code'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('forgot_password/', views.UserForgotPasswordView.as_view(), name='forgot_password'),
    path('verify_forgot_password/', views.VerifyForgotPasswordView.as_view(), name='verifyforgotpass'),
    path('newpassword/', views.NewPasswordView.as_view(), name='newpass'),
]
