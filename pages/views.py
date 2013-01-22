from django.shortcuts import render_to_response, get_object_or_404
from pages.models import Page

def home(request):
    #homepage = get_object_or_404(Page, pk = 1)
    return render_to_response('website/index.html')

def view(request, page_slug):
    page = get_object_or_404(Page, slug = page_slug)
    return render_to_response('website/page_view.html', {'page': page})