from django.db import models
from django.urls import reverse

# Create your models here.
from django.utils.text import slugify
from tinymce.models import HTMLField


class Blog(models.Model):
    title = models.CharField(max_length=255, unique=True)
    sub_title = models.CharField(max_length=255, blank=True, null=True)
    quote = models.TextField(null=True, blank=True)
    image_url = models.URLField()
    body = HTMLField(unique=True)
    slug = models.SlugField(blank=True, null=True, max_length=255)
    is_active = models.BooleanField(default=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.slug is None or len(self.slug) == 0:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("blog_details", args=[self.slug])
