# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from pages.models import Page, ContactForm
from django.utils.translation import ugettext as _

def home(request):
    #homepage = get_object_or_404(Page, pk = 1)
    return render_to_response('website/index.html', {'tweets': getTweets()})

def view(request, page_slug):
    page = get_object_or_404(Page, slug = page_slug)
    if (page_slug == 'contacto'):
        if request.method == 'POST':
            form = ContactForm(request.POST) # A form bound to the POST data
            if form.is_valid(): # All validation rules pass
                # Process the data in form.cleaned_data
                subject = form.cleaned_data['asunto']
                message = form.cleaned_data['mensaje']
                sender = form.cleaned_data['correo']
                
                recipients = ['zeroblend@davidvu']
                from django.core.mail import send_mail
                send_mail(subject, message, sender, recipients)
                
                return HttpResponseRedirect('/pagina/contacto') # Redirect after POST
            else:
                return render_to_response('website/page_view.html', {
                        'page': page,
                        'form': form,
                        'error_message': _("Por favor llene todos los campos."),
                }, context_instance=RequestContext(request))
        else:
            form = ContactForm()
                
            
    else:
        form = None
    return render_to_response('website/page_view.html', {'page': page, 'form': form}, context_instance=RequestContext(request))
    

"""def contact(request):
    page = get_object_or_404(Page, slug = 'contacto')
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            
            recipients = ['zeroblend@davidvu']
            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            
            return HttpResponseRedirect('/pagina/contacto') # Redirect after POST
    #else:
        #form = ContactForm() # An unbound form
    return render_to_response('website/page_view.html', {
            'page': page,
            'form': form,
            'error_message': _("Por favor llene todos los campos."),
    }, context_instance=RequestContext(request))"""

""" Funcion interna, no se llama por url """
def getTweets():
    tweets = []
    try:
        import twitter
        api = twitter.Api()
        latest = api.GetUserTimeline('zeroblend', count=2)
        for tweet in latest:
            status = tweet.text
            tweet_date = tweet.relative_created_at
            tweet_id = tweet.id
            tweets.append({'status': status, 'date': tweet_date, 'id': tweet_id})
    except:
        tweets.append({'status': _('Sígueme en @zeroblend'), 'date': ''})
    return {'tweets': tweets}