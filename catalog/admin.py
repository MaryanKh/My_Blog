from django.contrib import admin

# Register your models here.
from .models import Author, Post, BlogComment

# admin.site.register(Post)
# admin.site.register(Author)


class BlogCommentsInline(admin.TabularInline):
    """
    Used to show 'existing' blog comments inline below associated blogs
    """
    model = BlogComment
    max_num=0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth')
    pass


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('title', 'author')
    inlines = [BlogCommentsInline]
    pass
