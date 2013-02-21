from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from zangetsu.settings import MEDIA_ROOT

urlpatterns = patterns('',
    url(r"^static/(.*)$"    , "django.views.static.serve", {"document_root": MEDIA_ROOT, "show_indexes": True}),
    url(r"^comments/"       , include("django.contrib.comments.urls")),
    url(r'^admin/'          , include(admin.site.urls)),
    url(r"^blog/"           , include("blog.urls")),
    url(r"^"                , include("blog.urls")),
)
