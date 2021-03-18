from django.shortcuts import render,redirect

from django.http import HttpResponse



from .models import Tweet
from .forms import TweetForm

# Create your views here.



def index(request):

    tweets = Tweet.objects.order_by('-date_added')
    #comment = tweet.comment_set.all()
    



    return render(request, 'core/index.html', {'tweets': tweets})

def create_tweet(request):

    if request.method != 'POST':
        tweet = TweetForm()
    else:
        tweet = TweetForm(data=request.POST)

        if tweet.is_valid:
            tweet_obj = tweet.save(commit=False)
            tweet_obj.user = request.user
            tweet_obj.save()
            return(redirect('core:index'))

    return render(request, 'core/create_tweet.html', {'tweet': tweet})

def edit_tweet(request, tweet_id):
    tweet = Tweet.objects.get(id=tweet_id)
    
    if request.method != 'POST':
        form = TweetForm(instance=tweet)

    else:
        form = TweetForm(instance=tweet, data=request.POST)
        if form.is_valid:
            form.save()
            return redirect('core:index')

    return render(request, 'core/edit_tweet.html', {'tweet': tweet,'form':form})

    