from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
#from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'davidvu.views.home', name='home'),
    # url(r'^davidvu/', include('davidvu.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', 'pages.views.home'),
    url(r'^pagina/(?P<page_slug>.*)/$', 'pages.views.view'),
    url(r'^contact/', 'pages.views.contact'),
    url(r'^portafolio/$', 'portfolios.views.index'),
    url(r'^portafolio/(?P<company_slug>.*)/$', 'portfolios.views.detail'),
    url(r'^tinymce/', include('tinymce.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    url(r'^$', 'pages.views.home'),
)