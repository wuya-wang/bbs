from django.urls import re_path
from rest_framework import routers
from api import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet, basename="user"),
router.register(r'posts', views.PostViewSet, basename="post"),
urlpatterns = [re_path(r'authorizations', views.Authorization.as_view(), name="authorizations")]
urlpatterns += router.urls
