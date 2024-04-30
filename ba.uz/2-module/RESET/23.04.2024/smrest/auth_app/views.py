from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from blog.models import MyUser
from .serializers import MyUserSerializer


@api_view(['GET'])
def signin_view(request):
    if request.user.is_authenticated:
        return Response(
            data={
                'status': 'success',
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


@api_view(['POST'])
def logout_view(request):
    return Response(
        data={'logged_out': True},
        status=status.HTTP_200_OK
    )


class UserCreateAPIView(CreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUser

    def post(self, request):
        data = request.data
        user = User.objects.create(username=data['username'], email=data['email'],
                                   password=make_password(data['password']))
        user.save()
        data['user'] = user.id
        serializer = MyUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserListAPIView(ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class UserRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
