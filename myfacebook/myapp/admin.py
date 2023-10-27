from django.contrib import admin
from myapp.models import Userprofile,UserPost
# Register your models here.
admin.site.register(UserPost)
admin.site.register(Userprofile)