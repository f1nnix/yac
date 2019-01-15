from django.forms import ModelForm
from bookmarks.models import Bookmark


class BookmarkBaseForm(ModelForm):
    class Meta:
        model = Bookmark
        fields = ['url', ]
