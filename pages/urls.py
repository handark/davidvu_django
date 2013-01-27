from django.conf.urls import patterns, url

urlpatterns = patterns('pages.views',
    url(r'^(?P<page_slug>.*)/$', 'view', name="page-detail"),
)