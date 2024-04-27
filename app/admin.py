from django.contrib import admin
from .models import *

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=('id','title','description','priority','project','deadline')

admin.site.register(Task,TaskAdmin)