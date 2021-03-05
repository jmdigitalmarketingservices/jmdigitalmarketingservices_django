"""jmdigitalmarketingservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# VIEWS

from home import views as home
from about import views as about
from seo import views as seo
from social_media import views as social_media
from web_development import views as web_development
from graphic_design import views as graphic_design
from app_development import views as app_development
from contact import views as contact
from privacy import views as privacy
from term import views as term
from blog import views as blog

from blog.models import Blog


# STATIC SITE GENERATORS FUNCTIONS

from django_distill import distill_path


def get_index():
    return None


def get_all_blog():
    for post in Blog.objects.all():
        yield {'slug': post.slug}


urlpatterns = [
    path('admin/', admin.site.urls),
    distill_path('', home.view, name="home", distill_func=get_index),
    distill_path('', home.not_found_view, name="not_found", distill_func=get_index, distill_file="404.html"),
    distill_path('', home.cname_view, name="cname", distill_func=get_index, distill_file="CNAME"),
    distill_path('', home.sitemap_view, name="sitemap", distill_func=get_index, distill_file="sitemap.xml"),
    distill_path('', home.robots_txt_view, name="robots_txt", distill_func=get_index, distill_file="robots.txt"),
    distill_path('success/', home.form_success, name="form_success", distill_func=get_index),
    distill_path('about/', about.view, name="about", distill_func=get_index),
    distill_path('seo/', seo.view, name="seo", distill_func=get_index),
    distill_path('social-media-marketing/', social_media.view, name="social_media", distill_func=get_index),
    distill_path('web-development/', web_development.view, name="web_development", distill_func=get_index),
    distill_path('graphic-design/', graphic_design.view, name="graphic_design", distill_func=get_index),
    distill_path('app-development/', app_development.view, name="app_development", distill_func=get_index),
    distill_path('blog/', blog.view, name="blog", distill_func=get_index),
    distill_path('blog/<slug:slug>/', blog.details, name="blog_details", distill_func=get_all_blog),
    distill_path('contact/', contact.view, name="contact", distill_func=get_index),
    distill_path('privacy/', privacy.view, name="privacy", distill_func=get_index),
    distill_path('term/', term.view, name="term", distill_func=get_index),
]
