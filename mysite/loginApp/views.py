from django.views import generic
from django.shortcuts import render
from django.contrib.auth import login

from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.status import HTTP_201_CREATED, HTTP_500_INTERNAL_SERVER_ERROR

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from rest_framework import viewsets
from .serializers import RegisterSerializer, UserSerializer


# Create your views here.
def getUser(request):
    return render(request, 'index.html')


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': AuthToken.objects.create(user)[1]
        }, status=HTTP_201_CREATED)


class LoginView(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request=request,user=user)
        return super(LoginView, self).post(request=request,format=None)