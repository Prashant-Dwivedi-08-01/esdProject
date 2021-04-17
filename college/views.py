from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Councelling
from django.contrib import messages

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        messages.info(request, "You need to login first")
        return redirect('Home')
    else:
        return render(request, "college/index.html")

def councelling(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        course = request.POST['course']
        query = request.POST['query']
        date = request.POST['date']
        time = request.POST['time']

        newSession = Councelling()
        newSession.name = name
        newSession.email = email
        newSession.city = city
        newSession.state = state
        newSession.country = country
        newSession.course = course
        newSession.query = query
        newSession.session_date = date
        newSession.session_time = time

        newSession.save()
        return redirect('CollegeHome')