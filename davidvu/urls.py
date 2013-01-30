from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.views.generic.simple import direct_to_template
#from django.views.generic.simple import direct_to_template
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^robots\.txt$', direct_to_template, {'template': 'robots.txt', 'mimetype': 'text/plain'}),
)  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns('',
    url(r'^$', 'pages.views.home', name="home"),
    url(r'^pagina/', include('pages.urls')),
    url(r'^portafolio/', include('portfolios.urls')),
)