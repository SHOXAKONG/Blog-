from django.contrib import admin

from portfolio.models import Contact, Post

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass