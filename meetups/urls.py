from django.urls import path

from . import views

# Django looks for a variable specifically named 'urlpatterns'
# registers all urls for the app and which view functions should be executed
# when requests reach those urls
urlpatterns = [
    path('meetups/', views.index),  # our-domain.com/meetups
    path('meetups/<slug:meetup_slug>', views.meetup_details) # our-domain.com/meetups/<dynamic-path-segment>
]