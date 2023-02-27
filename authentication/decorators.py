from django.shortcuts import redirect
from django.http import HttpResponse


def allowed_users(allowed_roles=[]):
    def decorator(func):
        def wrapper_func(request, *args, **kwargs):
            permission = None

            if request.user.role == 1:
                permission = 'librarian'

            if permission in allowed_roles:
                return func(request, *args, **kwargs)
            else:
                return HttpResponse("You are haven't permission")
        return wrapper_func
    return decorator
