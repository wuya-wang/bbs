from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, AllowAny
from api import models, serializers, filters
from guardian.shortcuts import assign_perm


class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAdminUser,)
    # permission_classes = (AllowAny,)
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    filterset_class = filters.UserFilter


class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    filterset_class = filters.PostFilter


class Authorization(APIView):
    queryset = models.User.objects.all()
    permission_classes = (IsAdminUser,)

    @staticmethod
    def post(request):
        user_id = request.data["user"]
        perm = request.data["perm"]
        object_id = request.data["object"]
        user = models.User.objects.get(id=user_id)
        objects = models.User.objects.get(id=object_id)
        print(request.data)

        assign_perm(perm, user, objects)
        return Response(status=status.HTTP_200_OK, data="ok")
