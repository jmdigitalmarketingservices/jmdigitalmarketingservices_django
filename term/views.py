from django.shortcuts import render


# Create your views here.
from meta.views import Meta


def view(request):
    meta = Meta(
        title="Terms & Condition | J. M. Digital Marketing",
        og_title='Terms & Condition | J. M. Digital Marketing',
        twitter_title='Terms & Condition | J. M. Digital Marketing',
        schemaorg_title='Terms & Condition | J. M. Digital Marketing',
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
        object_type='Terms & Condition of J. M. Digital Marketing',
        description='JM Digital Marketing Services is a Toronto based digital marketing services agency. Our experts '
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
        'has_contact': False,
        'contact_header': 'GET A FREE SITE AUDIT',
        'meta': meta,
        'extra_meta': '<meta name="robots" content="noindex">'
    }
    return render(request, "term/index.html", context)
