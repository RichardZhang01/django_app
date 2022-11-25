from django.shortcuts import render

# Create your views here.

# Django invokes this function automatically


def index(request):
    meetups = [
        {'title': 'A First Meetup', 'location': 'Toronto', 'slug': 'a-first-meetup'},
        {'title': 'A Second Meetup', 'location': 'Ottawa', 'slug': 'a-second-meetup'},
    ]
    # request parses the file by finding specific Django-enabled code, executes them, then
    # returns the finished file to the browser
    return render(request, 'meetups/index.html', {
        'meetups': meetups  # Passes the meetups list under the key 'meetups' to our template
    })


def meetup_details(request, meetup_slug):
    selected_meetup = {'title': 'A First Meetup',
                       'description': 'This is the first meetup'}

    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetup['title'],
        'meetup_description': selected_meetup['description'],
    })
