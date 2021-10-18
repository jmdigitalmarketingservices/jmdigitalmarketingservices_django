from django.conf import settings
from django.urls import reverse_lazy
from meta.views import Meta


def get_prop(name: str, value: str):
    return 'property', name, value


common_meta_tags = {
    'twitter_card': settings.SEO_TWITTER_CARD,
    'twitter_site': settings.SEO_TWITTER_SITE,
    'twitter_creator': settings.SEO_TWITTER_CREATOR,
    'schemaorg_title': settings.SEO_SITE_NAME,
    'image': '',
    'image_object': {
        'url': '',
        'secure_url': '',
        'type': 'image/jpeg',
        'width': 1200,
        'height': 630,
        'alt': settings.SEO_SITE_NAME + ' Image',
    },
    'locale': settings.SEO_LOCALE,
    'image_height': 1230,
    'image_width': 630,
    'object_type': settings.SEO_SITE_TYPE,
    'site_name': settings.SEO_SITE_NAME,
}

common_meta_tags_extra_props = [
    ('http-equiv', 'Content-Type', 'text/html; charset=UTF-8'),
    ('name', 'robots', 'all'),
    get_prop('fb:profile_id', settings.SEO_FACEBOOK_ID + '/about/'),
    get_prop('og:locale', settings.SEO_LOCALE),
    get_prop('og:see_also', settings.SEO_INSTAGRAM_ID),
    get_prop('og:see_also', settings.SEO_LINKEDIN_ID),
    get_prop('og:see_also', settings.SEO_FACEBOOK_ID),
    get_prop('og:see_also', settings.SEO_TWITTER_ID),
]

home_meta_tags = Meta(
    **common_meta_tags,
    extra_custom_props=common_meta_tags_extra_props + [],
    title=settings.SEO_SITE_TITLE,
    description=settings.SEO_SITE_MAIN_DESCRIPTION,
)

SEO_PAGE_TITLE = 'SEO Toronto | SEO Company Toronto | SEO Services Toronto'
SEO_PAGE_DESCRIPTION = 'We are a leading SEO company in Toronto helping brands increase their ' \
                       'organic search engine traffic & revenue. Start your SEO campaign today!'
seo_meta_tags = Meta(
    **common_meta_tags,
    extra_custom_props=common_meta_tags_extra_props + [
        get_prop('og:url', reverse_lazy('seo')),
    ],
    title=SEO_PAGE_TITLE,
    description=SEO_PAGE_DESCRIPTION,
)

WEB_PAGE_TITLE = 'Web Design Company Toronto | Website Design Services Toronto'
WEB_PAGE_DESCRIPTION = 'J. M. Digital is #1 Toronto Web Design & Web Development Company with ' \
                       'over 10+ years of expertise as a website design agency for small & medium' \
                       ' size business and Brands.'

web_development_meta_tags = Meta(
    **common_meta_tags,
    extra_custom_props=common_meta_tags_extra_props + [
        get_prop('og:url', reverse_lazy('web_development')),
    ],
    title=WEB_PAGE_TITLE,
    description=WEB_PAGE_DESCRIPTION,
)

APP_PAGE_TITLE = 'Top App Developers Toronto | Mobile App Development Company in Toronto'
APP_PAGE_DESCRIPTION = 'Looking for the best app developers in Toronto to get your app built? ' \
                       'We are the best app development company in Toronto, creating a portfolio ' \
                       'of highly performantmobile apps for iOS &amp; Android.'

app_development_meta_tags = Meta(
    **common_meta_tags,
    extra_custom_props=common_meta_tags_extra_props + [
        get_prop('og:url', reverse_lazy('app_development')),
    ],
    title=APP_PAGE_TITLE,
    description=APP_PAGE_DESCRIPTION,
)
