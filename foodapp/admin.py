from django.contrib import admin
from .models import Category,Product

# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,catadmin)

class proadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug','stock','price','img']
    list_editable = ['stock','price','img']
admin.site.register(Product,proadmin)