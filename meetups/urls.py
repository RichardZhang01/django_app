from django.urls import path

from . import views

# Django looks for a variable specifically named 'urlpatterns'
# registers all urls for the app and which view functions should be executed
# when requests reach those urls
urlpatterns = [
    path('meetups/', views.index, name='all-meetups'),  # our-domain.com/meetups. name uniquely identifies this path
    path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-details') # our-domain.com/meetups/<dynamic-path-segment>
]