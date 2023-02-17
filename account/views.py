from django.shortcuts import get_object_or_404
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from .models import User
from .permissions import IsAuthor
from .serializers import RegistrationSerializer, \
LoginSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, \
ForgotPasswordCompleteSerializer, ReadInfoSerializer, \
UpdateUserSerializer
# from django.contrib.auth import logout


# class LogoutView(APIView):
#     def logout_view(request):
#         logout(request)


class RegistrationView(APIView):

    @swagger_auto_schema(request_body=RegistrationSerializer())
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(f'Аккаунт успешно создан, мы выслали вам' 
        'сообщение перейдите по ссылке, чтобы активировать аккаунт', 
        status=201)


class ActivationView(APIView):
    
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, 
        activation_code=activation_code).first()
        if not user:
            return Response('Пользователь не существует', status=400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Активирован', status=200)


class LoginView(ObtainAuthToken):
    
    serializer_class = LoginSerializer


class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    def delete(self, request):
        request.user.delete()
        return Response(status=204)


class UpdateUserView(APIView):
    permission_classes = [IsAuthenticated, IsAuthor]

    @swagger_auto_schema(request_body=UpdateUserSerializer())
    def patch(self, request):
        serializer = UpdateUserSerializer(request.user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=201)


class ReadInfoView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, email=None):
        if email is None:
            email = request.user.email
        user = get_object_or_404(User, email=email)
        return Response(ReadInfoSerializer(user).data)


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ChangePasswordSerializer())
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, 
        context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно обновлен')


class ForgotPasswordView(APIView):

    @swagger_auto_schema(request_body=ForgotPasswordSerializer())
    def post(self, request):
        serializer = ForgotPasswordSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.send_verification_email()
            return Response('Вам выслали сообщение для восстановления')


class ForgotPasswordCompleteView(APIView):

    @swagger_auto_schema(request_body=ForgotPasswordCompleteSerializer())
    def post(self, request):
        serializer = ForgotPasswordCompleteSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно изменен')
