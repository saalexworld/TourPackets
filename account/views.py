# from django.shortcuts import render
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
# from .permissions import IsActivePermission
from .serializers import RegistrationSerializer#, LoginSerializer, ChangePasswordSerializer, ForgotPasswordSerializer, ForgotPasswordCompleteSerializer #ActivationSerializer,
# from rest_framework.authtoken.models import Token
# from rest_framework.permissions import IsAuthenticated
from .models import User


class RegistrationView(APIView):
    @swagger_auto_schema(request_body=RegistrationSerializer())
    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(f'Аккаунт успешно создан, мы выслали вам сообщение, активируйте свой аккаунт отправив нам свой активационный код для активации', status=201)


class ActivationView(APIView):
    # @swagger_auto_schema(request_body=ActivationSerializer())
    def get(self, reqiuest, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('User does not exist', status=400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Activated', status=200)
    # def post(self, request):
        # serializer = ActivationSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.activate()
        # return Response('Аккаунт успешно активирован', status=200)


# class LoginView(ObtainAuthToken):
#     serializer_class = LoginSerializer

# class LogoutView(APIView):
#     permission_classes = [IsActivePermission]
#     def post(self, request):
#         user = request.user
#         Token.objects.filter(user=user).delete()
#         return Response('вы вышли со своего аккаунта')


# class ChangePasswordView(APIView):
#     permission_classes = [IsAuthenticated]

#     @swagger_auto_schema(request_body=ChangePasswordSerializer())
#     def post(self, request):
#         serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid(raise_exception=True):
#             serializer.set_new_password()
#             return Response('Status: 200. пароль успешно обновлен')


# class ForgotPasswordView(APIView):
#     @swagger_auto_schema(request_body=ForgotPasswordSerializer())
#     def post(self, request):
#         serializer = ForgotPasswordSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.send_verification_email()
#             return Response('Вам выслали сообщение для восстановления')


# class ForgotPasswordCompleteView(APIView):
#     @swagger_auto_schema(request_body=ForgotPasswordCompleteSerializer())
#     def post(self, request):
#         serializer = ForgotPasswordCompleteSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.set_new_password()
#             return Response('Пароль успешно изменен')
