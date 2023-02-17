from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .permissions import IsActivePermission
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from .models import User
from .serializers import RegistrationSerializer, ActivationSerializer , LoginSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, ForgotPasswordCompleteSerializer


class RegistrationView(APIView):
    @swagger_auto_schema(request_body=RegistrationSerializer())
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(f'Аккаунт успешно создан, мы выслали вам сообщение перейдите по ссылке, чтобы активировать аккаунт', status=201)


class ActivationView(APIView):
    
    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('Пользователь не существует', status=400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Активирован', status=200)


class LoginView(ObtainAuthToken):
    
    serializer_class = LoginSerializer


# class LogoutView(APIView):
#     permission_classes = [IsActivePermission]
#     @swagger_auto_schema
#     def post(self, request):
        # user = request.user
        # Token.objects.filter(user=user).delete()
        # return Response('Вы вышли со своего аккаунта')


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ChangePasswordSerializer())
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
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
