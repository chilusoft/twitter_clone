from django .urls import path

from . import views
app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('create_tweet', views.create_tweet, name='create_tweet'),
    path('<int:tweet_id>/edit', views.edit_tweet, name='edit_tweet')

]