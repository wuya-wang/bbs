from django.contrib import admin
from django.urls import path
from rest_framework import routers
from api import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet, basename="user"),
router.register(r'posts', views.PostViewSet, basename="post"),
urlpatterns = []
urlpatterns += router.urls
