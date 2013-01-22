from django.shortcuts import render_to_response, get_object_or_404
from portfolios.models import Company

def index(request):
    latest_companies = Company.objects.all().order_by('-pub_date')[:5]
    #output = ', '.join([c.company_name for c in latest_companies])
    return render_to_response('website/portfolio.html', {'latest_companies': latest_companies})
    """
    t = loader.get_template('companies/index.html')
    c = Context({
        'latest_companies': latest_companies,
    })
    return HttpResponse(t.render(c))
    """

def detail(request, company_slug):
    #return HttpResponse("Hello world, this is a test %s." % company_id)
    """try:
        c = Company.objects.get(pk=company_id)
    except Company.DoesNotExist:
        raise Http404
    """
    c = get_object_or_404(Company, slug = company_slug)
    return render_to_response('website/portfolio_detail.html', {'company': c})