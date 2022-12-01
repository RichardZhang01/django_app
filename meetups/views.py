from django.shortcuts import render, redirect

from .models import Meetup, Participant
from .forms import RegistrationForm

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
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration')
        
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': True,
            'meetup': selected_meetup,
            'form': registration_form
        })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', { # Many ways to handle an endpoint that does not exist. Can use a different template, redirects, etc.
            'meetup_found': False,
        })

def confirm_registration(request):
    return render(request, 'meetups/registration-success.html')