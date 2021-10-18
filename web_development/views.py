from django.shortcuts import render

from all_meta_tags import web_development_meta_tags


# Create your views here.


def view(request):
    meta = web_development_meta_tags
    context = {
        'has_contact': True,
        'contact_header': 'GET FREE CONSULTATION',
        'meta': meta
    }
    return render(request, "web_development/index.html", context)
