from django.contrib import admin
from .models import Roles, SideBarElement,PageBlock

# Register your models here.
admin.site.register(SideBarElement)
admin.site.register(PageBlock)