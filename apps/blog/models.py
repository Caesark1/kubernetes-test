from django.db import models

from .utils import unique_slugify


class Tag(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def save(self, **kwargs):
        slug_str = "%s" % self.title
        unique_slugify(self, slug_str)
        super(Tag, self).save(**kwargs)

    def __str__(self):
        return self.title


class Blog(models.Model):
    tag = models.ForeignKey(Tag, related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    body = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        slug_str = "%s" % self.title
        unique_slugify(self, slug_str)
        super(Blog, self).save(**kwargs)

    def __str__(self):
        return self.title
