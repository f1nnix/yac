from django import forms
from bookmarks.models import Bookmark


class BookmarkBaseForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['url', ]
        widgets = {
            'url': forms.TextInput(attrs={
                'class': 'form-control form-control-lg',
                'placeholder': 'Enter URL to save...',
                'autofocus': '',
            }),
        }
