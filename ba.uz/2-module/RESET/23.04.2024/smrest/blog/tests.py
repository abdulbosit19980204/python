from django.test import TestCase
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your tests here.
@api_view(['GET'])
def test(request):
    return Response(
        data={"test": "test"},
        status=status.HTTP_200_OK
    )
