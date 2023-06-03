from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import redirect

from .models import SideBarElement, Roles

def loadSidebarElements(view_func):
    def wrapped_func(request: WSGIRequest, *args, **kwargs):
        # check if it's regular user who has acess only to 'About me section'
        # or registered user with acess to additional sections such as my projects
        # or me - owner with acess to personal stuff (movies, notes, schedules and stuff)
        if request.user.groups.filter(name='USER').exists():
            sidebar = SideBarElement.objects.filter(content_acess=Roles.USER)
        elif not request.user.groups.filter(name='OWNER').exists():
            sidebar = SideBarElement.objects.exclude(content_acess=Roles.OWNER)
        else:
            sidebar = SideBarElement.objects.exclude(content_acess=Roles.OWNER)
        return view_func(request, sidebar, **kwargs)
    return wrapped_func

def authenticationRequired(view_func):
    def wrapped_func(request: WSGIRequest, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        else:
            return redirect("admin")
    return wrapped_func