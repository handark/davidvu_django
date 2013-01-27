from django.shortcuts import render_to_response, get_object_or_404
from portfolios.models import Company

def index(request):
    #output = ', '.join([c.company_name for c in latest_companies])
    all_companies = Company.objects.filter(category__name='Web').order_by('-pub_date')
    all_models = Company.objects.filter(category__name='3D').order_by('-pub_date')
    return render_to_response('website/portfolio.html', {'all_companies': all_companies, 'all_models': all_models})
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