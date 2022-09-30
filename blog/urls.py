from django.urls import include, path
from django.contrib.sitemaps.views import sitemap

from . import views
from .feeds import AtomSiteNewsFeed, LatestPostsFeed
from .sitemaps import PostSitemap

app_name = 'blog'

sitemaps = {
    "posts": PostSitemap,
}

urlpatterns = [
    path("feed/rss", LatestPostsFeed(), name="post_feed"),
    path("feed/atom", AtomSiteNewsFeed()),
    path("", views.PostList.as_view(), name="home"),
    path("<slug:slug>/", views.post_detail, name="post_detail"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
