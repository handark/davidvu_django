from django.db import models
from tinymce import models as tinymce_models

class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) 
    body = tinymce_models.HTMLField()
    
    def __unicode__(self):
        return self.title