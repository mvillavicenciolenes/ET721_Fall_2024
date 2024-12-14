from django.contrib import admin
#import the post model into the data base

from . models import Post

# Register your models here.

admin.site.register(Post)