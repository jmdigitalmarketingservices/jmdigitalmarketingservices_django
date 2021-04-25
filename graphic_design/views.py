from django.shortcuts import render


# Create your views here.
from meta.views import Meta


def view(request):
    meta_title = 'Professional Graphic Design | J. M. Digital Marketing Services'
    meta = Meta(
        title=meta_title,
        og_title=meta_title,
        twitter_title=meta_title,
        schemaorg_title=meta_title,
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
        object_type='Graphics Design',
        description='At J. M. Digital Marketing Services, we create unique graphic designs that represent your brand '
                    'and style. Call us for a free consultation +1(877) 861-5464',
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
    return render(request, "graphic_design/index.html", context)
