from django.shortcuts import render


# Create your views here.
from meta.views import Meta


def view(request):
    meta_title = "Web Design & Development | J. M. Digital Marketing Service"
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
        object_type='Web Design & Development',
        description='J. M. Digital Marketing Services turn your ideas into beautiful looking websites that are '
                    'responsive to any device. Free Site Audit Call +1(877) 861-5464',
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
    return render(request, "web_development/index.html", context)
