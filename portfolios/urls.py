from django.conf.urls import patterns, url

urlpatterns = patterns('portfolios.views',
    url(r'^$', 'index', name="portfolio-index"),
    url(r'^(?P<company_slug>.*)/$', 'detail', name="portfolio-detail"),
)