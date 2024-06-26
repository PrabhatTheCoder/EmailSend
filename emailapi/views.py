from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from emailapi.renderers import UserRenderer
from rest_framework import status
from rest_framework import serializers
from .serializers import EmailSerializer


# Create your views here.
class send_email(APIView):
    renderer_classes = [UserRenderer]
    
    def post(self, request, format = None):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'msg':'Email Sent. Please Check your Email'}, status= status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
