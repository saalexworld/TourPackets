from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)
    
from .views import RegistrationView, ActivationView, ChangePasswordView, \
ForgotPasswordView, ForgotPasswordCompleteView, DeleteUserView, \
UpdateUserView , ReadInfoView 


urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('activate/<str:email>/<str:activation_code>/', ActivationView.as_view(), name='activate'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('delete/', DeleteUserView.as_view(), name='delete'),
    path('update/', UpdateUserView.as_view(), name='update'),
    path('read_info/', ReadInfoView.as_view(), name='read_info'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot_password'),
    path('forgot_password_complete/', ForgotPasswordCompleteView.as_view(), name='forgot_password_complete')
]
