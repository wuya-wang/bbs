# -*- coding: utf-8 -*-
# @Author: wanghaoran
# @Time  : 2021/7/6 12:06
from rest_framework import permissions
from django.http import Http404
from rest_framework import exceptions


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class CustomPermission(permissions.BasePermission):

    perms_map = {
        # 将方法映射到所需的权限代码中,重写此字典自定义权限代码。eg:apis.add_users
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    authenticated_users_only = True

    def get_required_permissions(self, method, model_cls):
        """
        Given a model and an HTTP method, return the list of permission
        codes that the user is required to have.
        """
        kwargs = {
            'app_label': model_cls._meta.app_label,
            'model_name': model_cls._meta.model_name
        }

        if method not in self.perms_map:
            raise exceptions.MethodNotAllowed(method)

        return [perm % kwargs for perm in self.perms_map[method]]

    def _queryset(self, view):
        assert hasattr(view, 'get_queryset') \
            or getattr(view, 'queryset', None) is not None, (
            'Cannot apply {} on a view that does not set '
            '`.queryset` or have a `.get_queryset()` method.'
        ).format(self.__class__.__name__)

        if hasattr(view, 'get_queryset'):
            queryset = view.get_queryset()
            assert queryset is not None, (
                '{}.get_queryset() returned None'.format(view.__class__.__name__)
            )
            return queryset
        return view.queryset

    def has_permission(self, request, view):
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True
        if not request.user or (
                not request.user.is_authenticated and self.authenticated_users_only):
            return False

        queryset = self._queryset(view)
        perms = self.get_required_permissions(request.method, queryset.model)
        print(queryset.model)
        print(queryset, perms)
        print(request.user.has_perms(perms))
        return request.user.has_perms(perms)

    def has_object_permission(self, request, view, obj):
        # authentication checks have already executed via has_permission
        queryset = self._queryset(view)
        model_cls = queryset.model
        user = request.user
        perms = self.get_required_permissions(request.method, model_cls)
        print(perms, obj)
        print(user.has_perms(perms, obj))
        if not user.has_perms(perms, obj):
            # If the user does not have permissions we need to determine if
            # they have read permissions to see 403, or not, and simply see
            # a 404 response.

            if request.method in SAFE_METHODS:
                # Read permissions already checked and failed, no need
                # to make another lookup.
                print("1")
                raise Http404

            read_perms = self.get_required_permissions('GET', model_cls)
            if not user.has_perms(read_perms, obj):
                print(read_perms, "2")
                raise Http404

            # Has read permissions.
            return False

        return True
