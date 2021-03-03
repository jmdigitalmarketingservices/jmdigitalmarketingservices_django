from django.shortcuts import render

# Create your views here.


def view(request):
    context = {
        'title': 'SEO Digital Marketing Services Agency Toronto 📱 | J. M. Digital Marketing Services 🥇',
        'meta_description': 'Toronto&#039;s Best SEO Digital Marketing Agency Service for page #1🥇 ranking! Call 647-990-2414. FREE WEB ANALYSIS. Economical and affordable SEO and Social Media Services.',
        'extra_meta': '<meta name="robots" content="noindex">'
    }
    return render(request, "term/index.html", context)
