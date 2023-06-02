from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect

def loadSidebarElements(view_func):
    def wrapped_func(request, *args, **kwargs):
        if request.user.username == 'Lyra':
            print('wrapped Lyra')
        else:
            print('wrapped LyraHearthstrings')
        return view_func(request, *args, **kwargs)
    return wrapped_func

def authenticationRequired(view_func):
    def wrapped_func(request: WSGIRequest, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("admin")
    return wrapped_func