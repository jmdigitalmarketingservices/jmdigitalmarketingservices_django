from django.shortcuts import render


# Create your views here.
from meta.views import Meta


def view(request):
    meta = Meta(
        title="SEO Digital Marketing Services Agency Toronto | JM Digital",
        og_title='SEO Digital Marketing Services Agency Toronto | JM Digital',
        twitter_title='SEO Digital Marketing Services Agency Toronto | JM Digital',
        schemaorg_title='SEO Digital Marketing Services Agency Toronto | JM Digital',
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
        object_type='Website Home',
        description='JM Digital Marketing Services is a Toronto based digital marketing services agency. Our experts in the field of SEO and Social Media Marketing can help your website rank on Google, Bing & Yahoo. Call +1(877) 861-5464 for a FREE Website Audit Today!',
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
    return render(request, "home/index.html")
