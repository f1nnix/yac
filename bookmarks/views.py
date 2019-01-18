from django.views.generic.base import TemplateView
from bookmarks.forms import BookmarkBaseForm
from bookmarks.models import Bookmark, Tag
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.edit import FormView
from bookmarks.tasks import fetch_bookmark_mata


def find_or_create_tags(tags_titles):
    tags = []
    for tag_title in tags_titles:
        chunks = tag_title.split('/')
        if len(chunks) > 1:
            (parent_tag, target_tag,) = chunks[:2]
        else:
            tags.append(Tag.objects.get_or_create(
                title__iexact=tag_title,
                defaults={'title': tag_title, }
            )[0])

    return tags


class BookmarksView(FormView, TemplateView):
    template_name = 'bookmarks/bookmark_list.html'
    form_class = BookmarkBaseForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # process tags, excluded from validation
            # TODO: create custom Field
            tags = find_or_create_tags(request.POST.getlist('tags'))

            bookmark = form.save()
            bookmark.tags.set(tags)

            fetch_bookmark_mata.delay(bookmark.id)

            return redirect(reverse('bookmark-list'))

        generic_context = self.get_context_data()
        custom_context = {'form': form, }

        return render(request, self.template_name, {**generic_context, **custom_context})

    def get_context_data(self, *args, **kwargs):
        context = super(BookmarksView, self).get_context_data(*args, **kwargs)
        context['bookmarks'] = Bookmark.objects.all().order_by('-created_at').prefetch_related('tags')
        context['tags'] = Tag.objects.all()
        return context
