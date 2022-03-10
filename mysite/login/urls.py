# mysite_login/urls.py

from django.urls import path,re_path,include
from django.contrib import admin


from . import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^index/', views.index),
    re_path(r'^login/', views.login),
    re_path(r'^register/', views.register),
    re_path(r'^logout/', views.logout),
    re_path(r'^captcha', include('captcha.urls')),
]