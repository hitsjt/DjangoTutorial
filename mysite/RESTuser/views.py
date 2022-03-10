from django.shortcuts import render

from .models import User
from .serializers import UserSerializer

from rest_framework.generics import ListCreateAPIView


# Create your views here.

# ListCreateAPIView 获取列表数据，创建数据的类视图
# 获取全部用户
class UsersAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


# 获取单个用户
class UserAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
