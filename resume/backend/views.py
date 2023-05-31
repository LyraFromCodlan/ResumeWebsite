from django.shortcuts import render
from django.http import HttpResponse
# Basic request class added to read documentation
from django.core.handlers.wsgi import WSGIRequest

from .models import SideBarElement, Roles

# Create your views here.
def returnMainPage(request:WSGIRequest):
    return HttpResponse("THIS IS MAIN PAGE")

def sidebar(request:WSGIRequest):
    print(request.__class__.__name__)
    print(request.headers)
    side_bar=SideBarElement.objects.all().exclude(content_id=Roles.ADMIN)
    return render(request = request, template_name= 'backend/main_page.html', context={"side_bar":side_bar})

def posts(request:WSGIRequest):
    return render(request,'backend/post_list.html', {})