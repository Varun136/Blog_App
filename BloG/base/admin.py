from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title','category','created_on','updated_on']
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['created_on','updated_on']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','created_on','updated_on']