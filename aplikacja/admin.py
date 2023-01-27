from django.contrib import admin
from .models import Profile, Post, Comment


class CommentInline(admin.StackedInline):
    model = Comment


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'age', 'bio', 'profile_picture', 'status']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['description', 'picture', 'profile']
    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'image']
