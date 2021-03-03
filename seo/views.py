from django.shortcuts import render

# Create your views here.


def view(request):
    context = {
        'has_contact': True,
        'contact_header': 'GET A FREE SITE AUDIT',
        'title': 'SEO Digital Marketing Services Agency Toronto 📱 | J. M. Digital Marketing Services 🥇',
        'meta_description': 'Toronto&#039;s Best SEO Digital Marketing Agency Service for page #1🥇 ranking! Call 647-990-2414. FREE WEB ANALYSIS. Economical and affordable SEO and Social Media Services.'
    }
    return render(request, "seo/index.html", context)
