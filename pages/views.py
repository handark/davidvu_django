from django.shortcuts import render_to_response, get_object_or_404
from pages.models import Page

def home(request):
    #homepage = get_object_or_404(Page, pk = 1)
    return render_to_response('website/index.html', {'tweets': getTweets()})

def view(request, page_slug):
    page = get_object_or_404(Page, slug = page_slug)
    return render_to_response('website/page_view.html', {'page': page})

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
        tweets.append({'status': 'Sigueme en @zeroblend', 'date': ''})
    return {'tweets': tweets}