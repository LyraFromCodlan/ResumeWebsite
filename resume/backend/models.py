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

# Playing with permission
    class Meta:
        # difine table name in database
        db_table = "sidebar_elements"
        permissions = (
            ('permission_code','Friendly permition description'),
            )

    id : int = models.AutoField(primary_key=True,db_column="id", db_index=True)
    # name of the block
    name : str = models.CharField(max_length=50, db_column="name")
    # code to tie sidebar element with corresponding page block of content
    code: str = models.CharField(max_length=50, db_column="code") 
    # active status dependent on the role - used for administrating or showing blocks only I use
    active: bool = models.BooleanField(default=True, db_column="active")
    # used to show content based on user permissions 
    content_acess: int = EnumChoiceField(enum_class=Roles)
    # models.CharField(choices=Roles, blank=False, default=Roles.USER)

# Page blocks are used to switch between content block (about me, projects, education, etc.) on main page
class PageBlock(models.Model):
    class Meta:
        # define table name in database
        db_table="page_blocks"
    # id
    id: int = models.AutoField(primary_key=True, db_column="id", db_index=True)
    # code to optimize search of elements
    code: str = models.CharField(max_length=50, db_column="code")
    # content store as html page, which are rendered onto main_page 
    content = models.CharField(db_column="content")





