from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from meta.views import Meta
from django.contrib.sitemaps.views import sitemap
from django.contrib import sitemaps

# Create your views here.

"""
title: SEO Digital Marketing Services Agency Toronto | JM Digital
og_title: SEO Digital Marketing Services Agency Toronto | JM Digital
twitter_title: SEO Digital Marketing Services Agency Toronto | JM Digital
schemaorg_title: SEO Digital Marketing Services Agency Toronto | JM Digital
description: JM Digital Marketing Services is a Toronto based full-fledged digital marketing services agency. Our experts in the field of SEO and Social Media Marketing can help your website rank on Google, Bing & Yahoo. Call +1(877) 861-5464 for a FREE Website Audit Today!
keywords: seo toronto, social media marketing, toronto web design, digital marketing agency toronto, app developers toronto, local seo company, seo company near me, shopify expert toronto, social media marketing agency, toronto web development
url: https://jmdigitalmarketingservices.ca/
image: https://jmdigitalmarketingservices.ca/static/images/logo-transparent.png
image_object: 
image_width: 464
image_height: 118
object_type: 
site_name: JM Digital Marketing Services
twitter_site
twitter_creator
twitter_type
facebook_app_id
locale: toronto

"""


def view(request):
    meta = Meta(
        title="SEO Digital Marketing Services Agency Toronto | JM Digital",
        og_title='SEO Digital Marketing Services Agency Toronto | JM Digital',
        twitter_title='SEO Digital Marketing Services Agency Toronto | JM Digital',
        schemaorg_title='SEO Digital Marketing Services Agency Toronto | JM Digital',
        image='',
        image_object={
            'url': '',
            'secure_url': '',
            'type': 'image/jpeg',
            'width': 1200,
            'height': 630,
            'alt': 'JM Digital Marketing Services Image',
        },
        image_height=1230,
        image_width=630,
        object_type='Website Home',
        description='JM Digital Marketing Services is a Toronto based digital marketing services agency. Our experts in the field of SEO and Social Media Marketing can help your website rank on Google, Bing & Yahoo. Call +1(877) 861-5464 for a FREE Website Audit Today!',
        site_name='JM Digital Marketing Services',
        # keywords=[
        #     'seo toronto', 'social media marketing', 'toronto web design',
        #     'digital marketing agency toronto', 'app developers toronto',
        #     'local seo company', 'seo company near me', 'shopify expert toronto',
        #     'social media marketing agency', 'toronto web development'
        # ],
        extra_custom_props=[
            ('http-equiv', 'Content-Type', 'text/html; charset=UTF-8'),
        ]
    )
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
