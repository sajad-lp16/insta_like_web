from django.contrib import admin
from . import models


class PostMediaInline(admin.TabularInline):
    model = models.Media


class UserTagInline(admin.TabularInline):
    model = models.UserTag


class PostTagInline(admin.TabularInline):
    model = models.PostTag


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'location')
    inlines      = (PostMediaInline,)


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines      = (PostTagInline, UserTagInline)
