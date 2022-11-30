from django.shortcuts import render

from .models import Meetup

# Create your views here.

# Django invokes this function automatically


def index(request):
    meetups = Meetup.objects.all()
    # request parses the file by finding specific Django-enabled code, executes them, then
    # returns the finished file to the browser
    return render(request, 'meetups/index.html', {
        'meetups': meetups # Passes the meetups list under the key 'meetups' to our template
    })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)

        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', { # Many ways to handle an endpoint that does not exist. Can use a different template, redirects, etc.
            'meetup_found': False,
        })
