from django.shortcuts import render


# Create your views here.
from meta.views import Meta


def view(request):
    meta = Meta(
        title="SEO Toronto Company | J. M. Digital Marketing Services Agency",
        og_title='SEO Toronto Company | J. M. Digital Marketing Services Agency',
        twitter_title='SEO Toronto Company | J. M. Digital Marketing Services Agency',
        schemaorg_title='SEO Toronto Company | J. M. Digital Marketing Services Agency',
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
        object_type='SEO Toronto Company | J. M. Digital Marketing Services Agency',
        description='GROW YOUR TRAFFIC, LEADS & REVENUE with our SEO Toronto Company. Get A FREE Site Audit Today.',
        site_name='JM Digital Marketing Services',
        extra_custom_props=[
            ('http-equiv', 'Content-Type', 'text/html; charset=UTF-8'),
        ]
    )
    context = {
        'has_contact': True,
        'contact_header': 'GET A FREE SITE AUDIT',
        'meta': meta
    }
    return render(request, "seo/index.html", context)
