from django.shortcuts import render


# Create your views here.
from meta.views import Meta

from all_meta_tags import seo_meta_tags


def view(request):
    meta = seo_meta_tags
    print(seo_meta_tags.extra_custom_props)
    context = {
        'has_contact': True,
        'contact_header': 'GET A FREE SITE AUDIT',
        'meta': meta
    }
    return render(request, "seo/index.html", context)
