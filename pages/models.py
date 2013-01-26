from django.db import models
from django import forms
from django.utils.translation import ugettext_lazy as _
from tinymce import models as tinymce_models

class Page(models.Model):
    title = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    slug = models.SlugField(unique=True) 
    body = tinymce_models.HTMLField()
    body_en = tinymce_models.HTMLField()
    
    def __unicode__(self):
        return self.title
    
class ContactForm(forms.Form):
    asunto = forms.CharField(max_length=100, label=_('Asunto'))
    mensaje = forms.CharField(label=_('Mensaje'))
    correo = forms.EmailField(label=_('Correo'))
    #cc_myself = forms.BooleanField()