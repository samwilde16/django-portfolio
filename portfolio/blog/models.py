from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        all_posts = self.get_children().live().order_by('-first_published_at')
        # Paginate all posts by 5 per page
        paginator = Paginator(all_posts, 5)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["posts"] = posts
        return context





    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    # Parent page / subpage type rules
    parent_page_types = ['home.HomePage']
    subpage_types = ['blog.BlogPage']

    max_count = 1 

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
    ]

    # Parent page / subpage type rules
    parent_page_types = ['blog.BlogIndexPage']
    subpage_types = []