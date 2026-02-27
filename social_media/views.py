from django.shortcuts import render


# Create your views here.
from meta.views import Meta


def view(request):
    meta = Meta(
        title="Social Media Internet Marketing | J. M. Digital Marketing",
        og_title='Social Media Internet Marketing | J. M. Digital Marketing',
        twitter_title='Social Media Internet Marketing | J. M. Digital Marketing',
        schemaorg_title='Social Media Internet Marketing | J. M. Digital Marketing',
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
        object_type='Social Media Marketing',
        description='J. M. Digital Marketing Services helps create brand awareness by targeting key audiences on '
                    'social media platforms. Free Site Audit Call +1(877) 861-5464',
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
        'contact_header': 'GET FREE CONSULTATION',
        'meta': meta
    }
    return render(request, "social_media/index.html", context)
