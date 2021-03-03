from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def view(request):
    context = {
        'title': 'SEO Digital Marketing Services Agency Toronto 📱 | J. M. Digital Marketing Services 🥇',
        'meta_description': 'Toronto&#039;s Best SEO Digital Marketing Agency Service for page #1🥇 ranking! Call 647-990-2414. FREE WEB ANALYSIS. Economical and affordable SEO and Social Media Services.'
    }
    return render(request, "home/index.html", context)


def not_found_view(request):
    context = {
        'title': 'SEO Digital Marketing Services Agency Toronto 📱 | J. M. Digital Marketing Services 🥇',
        'meta_description': 'Toronto&#039;s Best SEO Digital Marketing Agency Service for page #1🥇 ranking! Call 647-990-2414. FREE WEB ANALYSIS. Economical and affordable SEO and Social Media Services.',
        'extra_meta': '<meta name="robots" content="noindex">'
    }
    return render(request, "404.html", context)


def cname_view(request):
    return HttpResponse(content="jmdigitalmarketingservices.ca", content_type="text/plain")
