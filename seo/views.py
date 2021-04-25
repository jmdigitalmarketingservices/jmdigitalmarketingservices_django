from django.shortcuts import render


# Create your views here.
from meta.views import Meta


def view(request):
    meta = Meta(
        title="SEO Social Media Web & App Development | J. M. Digital",
        og_title='SEO Social Media Web & App Development | J. M. Digital',
        twitter_title='SEO Social Media Web & App Development | J. M. Digital',
        schemaorg_title='SEO Social Media Web & App Development | J. M. Digital',
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
        object_type='SEO with J. M. Digital Marketing Services',
        description='J. M. Digital Marketing Services helps you increase traffic using organic & paid strategies on '
                    'social media networks. Free Site Audit Call +1(877) 861-5464',
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
        'contact_header': 'GET A FREE SITE AUDIT',
        'meta': meta
    }
    return render(request, "seo/index.html", context)
