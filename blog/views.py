from django.shortcuts import render
from blog.models import Blog
from django.shortcuts import get_object_or_404

# Create your views here.


def view(request):
    queryset = Blog.objects.all()
    context = {
        'blogs': queryset,
        'has_contact': True,
        'contact_header': 'GET A FREE SITE AUDIT',
        'title': 'SEO Digital Marketing Services Agency Toronto 📱 | J. M. Digital Marketing Services 🥇',
        'meta_description': 'Toronto&#039;s Best SEO Digital Marketing Agency Service for page #1🥇 ranking! Call 647-990-2414. FREE WEB ANALYSIS. Economical and affordable SEO and Social Media Services.'
    }
    return render(request, "blog/index.html", context)


def details(request, slug):
    queryset = Blog.objects.all()
    blog = get_object_or_404(queryset, slug=slug)
    context = {
        'blog': blog,
        'has_contact': True,
        'contact_header': 'GET A FREE SITE AUDIT',
        'title': 'SEO Digital Marketing Services Agency Toronto 📱 | J. M. Digital Marketing Services 🥇',
        'meta_description': 'Toronto&#039;s Best SEO Digital Marketing Agency Service for page #1🥇 ranking! Call 647-990-2414. FREE WEB ANALYSIS. Economical and affordable SEO and Social Media Services.'
    }
    return render(request, 'blog/details/index.html', context)
