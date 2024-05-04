from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from blog.models import MyUser
from .serializers import MyUserSerializer, UserSerializer


@api_view(['GET'])
def signin_view(request):
    if request.user.is_authenticated:
        return Response(
            data={
                'status': 'success',
                'user': UserSerializer(request.user).data,
                'message': 'User logged in'
            },
            status=status.HTTP_200_OK
        )
    return Response(
        status=status.HTTP_401_UNAUTHORIZED,
        data={
            "message": "You are not logged in"
        }
    )


class UserCreateAPIView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUser

    def post(self, request):
        data = request.data
        is_registered = User.objects.filter(username=data['username']).exists()
        # print(is_registered)
        if is_registered is False:
            user = User.objects.create(username=data['username'], email=data['email'],
                                       password=make_password(data['password']))
            user.save()
            data['user'] = user.id
            serializer = MyUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data={
                    "user": serializer.data,
                    "status": "Registered",
                }, status=status.HTTP_201_CREATED)
        return Response(
            status=status.HTTP_409_CONFLICT,
            data={
                'message': 'User already exists',
                'notification': 'username and email must be unique',
            }
        )


class UserListAPIView(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
    permission_classes = [IsAuthenticated]
