from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def register_view(request):
    return Response(
        data={
            'status': 'success',
            'message': 'User registered successfully'
        },
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def signin_view(request):
    return Response(
        data={
            'status': 'success',
            'message': 'User logged in'
        },
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
def logout_view(request):
    return Response(
        data={'logged_out': True},
        status=status.HTTP_200_OK
    )
