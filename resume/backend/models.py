from django.db import models
from enumchoicefield import ChoiceEnum,EnumChoiceField

# enum class for Roles
class Roles(ChoiceEnum):
    # user have only rights to read contents of the main page of the resume
    USER = 'USER'
    # view-admin has additional rights to view admin panel in read-only mode
    VIEW_ADMIN = 'VIEW_ADMIN'
    # admin can change contents and elements of the website
    ADMIN = 'ADMIN'
    # owner, as me, has acess to the contents I store for personal use
    OWNER = 'OWNER'


# Model is used to depict the sidebar on the main page
class SideBarElement(models.Model):
    id : int = models.AutoField(primary_key=True,db_column="id")
    # name of the block
    name : str = models.CharField(max_length=50, db_column="name")
    # active status dependent on the role - used for administrating or showing blocks only I use
    active: bool = models.BooleanField(default=True, db_column="active")
    content_id: int = EnumChoiceField(enum_class=Roles,)
    # models.CharField(choices=Roles, blank=False, default=Roles.USER)



