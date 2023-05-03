from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

def csrf_exempt_class(view_class):
    view_class.dispatch = method_decorator(csrf_exempt)(view_class.dispatch)
    return view_class
