from django.shortcuts import get_object_or_404
from django.shortcuts import render
from meta.views import Meta

from blog.models import Blog


# Create your views here.


def view(request):
    queryset = Blog.objects.all()
    meta = Meta(
        title="SEO Digital Marketing Services Agency Toronto | J. M. Digital",
        og_title='SEO Digital Marketing Services Agency Toronto | J. M. Digital',
        twitter_title='SEO Digital Marketing Services Agency Toronto | J. M. Digital',
        schemaorg_title='SEO Digital Marketing Services Agency Toronto | J. M. Digital',
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
        object_type='Blog of J. M. Digital Marketing Services',
        description='J. M. Digital Marketing Services is a Toronto based digital marketing services agency. Our '
                    'experts '
                    'in the field of SEO and Social Media Marketing can help your website rank on Google, '
                    'Bing & Yahoo. Call +1(877) 861-5464 for a FREE Website Audit Today!',
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
        'blogs': queryset,
        'has_contact': True,
        'contact_header': 'GET A FREE SITE AUDIT',
        'meta': meta
    }
    return render(request, "blog/index.html", context)


def details(request, slug):
    queryset = Blog.objects.filter(is_active=True)
    blog = get_object_or_404(queryset, slug=slug)
    context = {
        'blog': blog,
        'has_contact': True,
        'contact_header': 'GET A FREE SITE AUDIT',
        'title': 'SEO Digital Marketing Services Agency Toronto 📱 | J. M. Digital Marketing Services 🥇',
        'meta_description': 'Toronto&#039;s Best SEO Digital Marketing Agency Service for page #1🥇 ranking! Call 647-990-2414. FREE WEB ANALYSIS. Economical and affordable SEO and Social Media Services.'
    }
    return render(request, 'blog/details/index.html', context)
