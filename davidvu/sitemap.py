from django.contrib.sitemaps import Sitemap
from pages.models import Page
from portfolios.models import Company

class StaticSitemap(Sitemap):
    #priority = 0.5
    lastmod = None
 
    def items(self):
        return [
                "/",
                ("/portafolio/", "weekly", "1")
            ]
 
    def location(self, obj):
        return obj[0] if isinstance(obj, tuple) else obj
 
    def changefreq(self, obj):
        return obj[1] if isinstance(obj, tuple) else "monthly"
    
    def priority(self, obj):
        return obj[2] if isinstance(obj, tuple) else "0.5"

class PageSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.5

    def items(self):
        return Page.objects.all()

class PortfolioSitemap(Sitemap):
    changefreq = "yearly"
    priority = 0.7

    def items(self):
        return Company.objects.all()