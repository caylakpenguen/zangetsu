# -*- coding: utf-8 -*-
#
# Copyright © 2006, 2007, 2008, 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

import datetime

from django.conf.urls import patterns, url

from blog.feeds import RssFeed, AtomFeed
from blog.models import Entry
from blog.sitemap import ZangetsuSitemap
from blog import views

Now = datetime.datetime.now


info_dict = {
    "queryset": Entry.objects.filter(pubdate__lte=Now()),
    "date_field": "pubdate",
}

sitemaps = {
    "blog": ZangetsuSitemap
}

urlpatterns = patterns("",
    (r"^search/$", "blog.views.search"),

    (r"^comments/$", "blog.views.recent_comments"),

    (r"^comments/page/(?P<page>\d+)/$", "blog.views.recent_comments"),

    (r"^tag/(?P<slug>.*)/page/(?P<page>\d+)/$", "blog.views.tags"),

    (r"^tag/(?P<slug>.*)/$", "blog.views.tags"),

    (r"^entry/(?P<object_id>\d+)/$",
        "django.views.generic.list_detail.object_detail",
        {"queryset": Entry.objects.filter(pubdate__lte=Now())}
    ),

    (r"^feed/rss/(?P<category_title>.*)/$", RssFeed()),

    (r"^feed/rss/(?P<category_title>.*)/$", AtomFeed()),

    (r"^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\w{1,2})/(?P<object_id>\d+)/$",
        "django.views.generic.date_based.object_detail",
        dict(info_dict, month_format="%m")
    ),

    (r"^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\w{1,2})/$",
        "django.views.generic.date_based.archive_day",
        dict(info_dict, month_format="%m")
    ),

    (r"^(?P<year>\d{4})/(?P<month>\d{1,2})/$",
        "django.views.generic.date_based.archive_month",
        dict(info_dict, month_format="%m")
    ),

    (r"^(?P<year>\d{4})/$",
        "django.views.generic.date_based.archive_year",
        info_dict
    ),

    (r"^page/(?P<page>\d+)/$", "blog.views.all_entries"),

    (r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),

    (r"^/?$", "blog.views.all_entries"),
)
