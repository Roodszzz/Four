from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_image/', null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(null=True, blank=True)


