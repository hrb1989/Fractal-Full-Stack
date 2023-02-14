from django.contrib import admin

# Register your models here.
from .models import Name

class modelAdmin(admin.ModelAdmin):
    list_display = ("fname", "lname")

admin.site.register(Name, modelAdmin)