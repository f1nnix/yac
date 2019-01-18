import extraction
import requests
from celery.decorators import task
from bookmarks.models import Bookmark


@task(name="fetch_bookmark_mata")
def fetch_bookmark_mata(bookmark_id):
    try:
        bookmark = Bookmark.objects.get(id=bookmark_id)
        html = requests.get(bookmark.url).text
        extracted = extraction.Extractor().extract(html, source_url=bookmark.url)
        bookmark.title = extracted.title
        bookmark.description = extracted.description
        bookmark.save()
    except Bookmark.DoesNotExist:
        print('Bookmark id=%s not found')
    except:
        # TODO: handle network errors
        pass
