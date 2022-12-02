from django.urls import path

from . import views

# Django looks for a variable specifically named 'urlpatterns'
# registers all urls for the app and which view functions should be executed
# when requests reach those urls
urlpatterns = [
    # our-domain.com/meetups. name uniquely identifies this path
    path('', views.index, name='all-meetups'),
    path('<slug:meetup_slug>/success', views.confirm_registration,
         name='confirm-registration'),
    # our-domain.com/meetups/<dynamic-path-segment>
    path('<slug:meetup_slug>',
         views.meetup_details, name='meetup-details')
]
