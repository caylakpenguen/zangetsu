# -*- coding: utf-8 -*-
#
# Copyright © 2006, 2007, 2008, 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from django.contrib.syndication.views import Feed

from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404

from blog.models import Entry, Tag
from blog import defaults
from zangetsu.settings import URL
import datetime

class RSSFeed(Feed):
    title = defaults.BLOG_NAME
    link = URL
    description = defaults.BLOG_DESC

    def get_object(self, request, category_title):
    return get_object_or_404(Tag, title=category_title)

    def items(self, object):
        now = datetime.datetime.now()
        if object is None:
            result = Entry.objects
        else:
            result = object.entry_set.all()

        return result.filter(pubdate__lte=now).order_by("-pubdate")[:defaults.RSS_ITEM_NUMBER]

    def item_pubdate(self, item):
        return item.pubdate

class AtomFeed(RSSFeed):
    subtitle = RSSFeed.description
    feed_type = Atom1Feed
