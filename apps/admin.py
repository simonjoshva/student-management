from django.contrib import admin
from apps.models import student
class studentadmin(admin.ModelAdmin):
    list_display=['idno','name','age','course','email']
admin.site.register(student,studentadmin)

# Register your models here.
