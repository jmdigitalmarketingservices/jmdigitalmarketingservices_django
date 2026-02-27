from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
from all_meta_tags import home_meta_tags


def view(request):
    meta = home_meta_tags
    context = {
        'has_contact': True,
        'contact_header': 'GET A FREE SITE AUDIT',
        'meta': meta
    }

    return render(request, "home/index.html", context)


def not_found_view(request):
    context = {
        'has_contact': False,
        'contact_header': 'GET A FREE SITE AUDIT',
        'title': 'SEO Digital Marketing Services Agency Toronto 📱 | J. M. Digital Marketing Services 🥇',
        'meta_description': 'Toronto&#039;s Best SEO Digital Marketing Agency Service for page #1🥇 ranking! Call 647-990-2414. FREE WEB ANALYSIS. Economical and affordable SEO and Social Media Services.',
        'extra_meta': '<meta name="robots" content="noindex">'
    }
    return render(request, "404.html", context)


def form_success(request):
    context = {
        'has_contact': False,
        'contact_header': 'GET A FREE SITE AUDIT',
        'title': 'SEO Digital Marketing Services Agency Toronto 📱 | J. M. Digital Marketing Services 🥇',
        'meta_description': 'Toronto&#039;s Best SEO Digital Marketing Agency Service for page #1🥇 ranking! Call 647-990-2414. FREE WEB ANALYSIS. Economical and affordable SEO and Social Media Services.',
        'extra_meta': '<meta name="robots" content="noindex">'
    }
    return render(request, "success.html", context)


def cname_view(request):
    return HttpResponse(content="jmdigitalmarketingservices.ca", content_type="text/plain")


def sitemap_view(request):
    return render(request, "sitemap.xml", content_type="text/xml")


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return [
            'home', 'about', 'seo',
            'social_media', 'web_development',
            'graphic_design', 'app_development',
        ]

    def location(self, item):
        return reverse(item)


def sitemap_view_2(request):
    sitemaps_ = {
        'static': StaticViewSitemap,
    }
    return sitemap(request=request, sitemaps=sitemaps_)


def robots_txt_view(request):
    return render(request, "robots.txt", content_type="text/txt")
