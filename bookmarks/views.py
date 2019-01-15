from django.views.generic.base import TemplateView
from bookmarks.forms import BookmarkBaseForm
from bookmarks.models import Bookmark
from django.shortcuts import render
from django.views.generic.edit import FormView


class BookmarksView(FormView, TemplateView):
    template_name = 'bookmarks/bookmark_list.html'
    form_class = BookmarkBaseForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            form = self.form_class()

        generic_context = self.get_context_data()
        custom_context = {'form': form, }

        return render(request, self.template_name, {**generic_context, **custom_context})

    def get_context_data(self, *args, **kwargs):
        context = super(BookmarksView, self).get_context_data(*args, **kwargs)
        context['bookmarks'] = Bookmark.objects.all().order_by('-created_at')

        return context
