from django.contrib import admin
from  blog.models import Post, BlogComment
# Register your models here.
admin.site.register((BlogComment))
@admin.register(Post)  #changing admin and registering model
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ("tinyInject.js",)
# admin.site.register((BlogComment,Post))