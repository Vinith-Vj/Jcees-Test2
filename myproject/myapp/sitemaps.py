from django.contrib.sitemaps import Sitemap
from .models import Boat, BoatingPackage, Property
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'monthly'

    def items(self):
        return ['boat', 'contact']
    
    def location(self, item):
        return reverse(item)

class BoatSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Boat.objects.all()
    
    def location(self, obj):
        return reverse('boat', kwargs={'slug': obj.slug})
    
class BoatingPackageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return BoatingPackage.objects.all()
    
    def location(self, obj):
        return reverse('package', kwargs={'slug': obj.slug})
    
class PropertySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Property.objects.all()
    
    def location(self, obj):
        return reverse('property', kwargs={'slug': obj.slug})