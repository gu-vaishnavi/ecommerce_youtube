from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class Home(APIView):
    authentication_classes = [JWTAuthentication]
    permission_class = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Hello world'}
        return Response(content)


def register(request):
    if request.method == "GET":
        return render(request, 'UsersApp/register.html')
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        return HttpResponse('<h1></h1>')
        
