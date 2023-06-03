from django.shortcuts import render
from django.http import HttpResponse
# Basic request class added to read documentation
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

from .models import SideBarElement, Roles
from .decorators import loadSidebarElements, authenticationRequired

# Create your views here.
@login_required(redirect_field_name="admin/")
def returnMainPage(request:WSGIRequest):
    return HttpResponse("THIS IS MAIN PAGE")

@authenticationRequired
@loadSidebarElements
def sidebar(request:WSGIRequest, *args, **kwargs):
    side_bar=args[0]
    return render(request = request, template_name= 'backend/main_page.html', context={"side_bar":side_bar,"block": "some data"})

def posts(request:WSGIRequest):
    return render(request,'backend/post_list.html', {})

@loadSidebarElements
def onclick(request: WSGIRequest):
    side_bar=SideBarElement.objects.all()
    print(request.user.groups.all())
    print(request.user.username)
    return render(request = request, template_name= 'backend/main_page.html', context={"side_bar":side_bar,"block": "some data"})