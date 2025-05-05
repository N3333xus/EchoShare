from django.db import models
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name='items')
    article_image = models.ImageField(upload_to='cover_images/', blank=True, null=True)
    title = models.CharField(max_length=255)
    text = CKEditor5Field('Text', config_name='extends')
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    date_posted = models.DateField(default=timezone.now)
    url = models.CharField(max_length=200, null=True, blank=True, unique=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class About(models.Model):
    title = models.CharField(max_length=255, null=True)
    about_text = CKEditor5Field('Text', config_name='extends')
    
    def save(self, *args, **kwargs):
        existing_count = About.objects.count()
        
        if existing_count == 0:
            super().save(*args, **kwargs)
        else:

            if self.pk:
                super().save(*args, **kwargs)
            else:
                raise Exception("Only one instance of About is allowed.")

    def __str__(self):
        return self.title