from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from tinymce import models as tinymce_models

class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) 
    body = tinymce_models.HTMLField()
    
    def __unicode__(self):
        return self.title
    
class ContactForm(forms.Form):
    asunto = forms.CharField(max_length=100)
    mensaje = forms.CharField(_('mensaje'))
    correo = forms.EmailField(_('correo'))
    #cc_myself = forms.BooleanField()