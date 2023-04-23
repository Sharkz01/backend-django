from django.contrib import admin
from .models import *

class PostJobAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'company', 'link', 'post', 'description', 'agency')

# Register your models here.
admin.site.register(PostJob, PostJobAdmin)