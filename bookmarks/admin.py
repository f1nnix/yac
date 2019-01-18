from django.contrib import admin
from bookmarks.models import Bookmark, Tag


# Register your models here.
class BookmarkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Tag, )
