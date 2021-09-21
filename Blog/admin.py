from django.contrib import admin
from .models import BlogPost, Supply_Categorys, General_Supplies, BlogComment, Categorys, About, Main_Service, Contact, Home_Layout, User_Profile
# Register your models here.

admin.site.register(BlogPost)
admin.site.register(BlogComment)
admin.site.register(Categorys)
admin.site.register(About)
admin.site.register(Main_Service)
admin.site.register(Contact)
admin.site.register(Home_Layout)
admin.site.register(User_Profile)
admin.site.register(Supply_Categorys)
admin.site.register(General_Supplies)