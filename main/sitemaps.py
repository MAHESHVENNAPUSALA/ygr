from django.contrib.sitemaps import Sitemap

class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return [
            '/',
            '/demo/',
            '/services/',
            '/aboutus/',
            '/careers/',
            '/contact/',
        ]

    def location(self, item):
        return item