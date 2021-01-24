from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .models import Timesheet
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib.auth.models import Group
from django.contrib import messages

from .models import *

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .models import *
from .filters import TimesheetFilter
import datetime


# Create your views here.

def go_index(request):
    return render(request, 'timesheet/index.html')


def go_connexion(request):
    return render(request, 'registration/login.html')


def go_deconnexion(request):
    return render(request, 'registration/logged_out.html')


def go_accueil_client(request):
    return render(request, 'timesheet/client_accueil.html')


def go_accueil_admin(request):
    return render(request, 'timesheet/admin_accueil.html')


def go_accueil_employe(request):
    return render(request, 'timesheet/employe_accueil.html')


def login_success(request):
    """Pour l'authentification https://www.youtube.com/results?search_query=django+login+success"""
    if request.user.groups.filter(name="clients").exists():
        return redirect("go_accueil_client")
    if request.user.groups.filter(name="admin").exists():
        return redirect("go_accueil_admin")
    if request.user.groups.filter(name="employe").exists():
        return redirect("go_accueil_employe")
    else:
        return redirect('go_connexion')


def go_timesheet_emp(request):
    timesheet = Timesheet.objects.all()
    return render(request, 'timesheet/consulter_timesheet.html', {'timesheets': timesheet})


def go_timesheet_admin(request):
    """lien pour la condition https://www.youtube.com/watch?v=yhDJrCJQbfI"""
    timesheet_admin = Timesheet.objects.all()
    search_query = request.GET.get('search', '')
    if search_query:
        posts = Timesheet.objects.filter(date=search_query)
    else:
        posts = Timesheet.objects.all()


    return render(request, 'timesheet/timesheet_admin.html', {'posts': posts})


def go_emp_ts(request):
    timesheet_admin_emp = Timesheet.objects.all()
    search_query_emp = request.GET.get('search_emp','')
    if search_query_emp:
        emp = Timesheet.objects.filter(employe=search_query_emp)
    else:
        emp = Timesheet.objects.all()

    return render(request, 'timesheet/timesheet_admin_emp.html', {'emp': emp})

def go_timesheet_admin_emp(request):
    timesheet_admin_emp = Timesheet.objects.all()
    search_query_emp = request.GET.get('search_emp', '')

    if search_query_emp:
        emp = Timesheet.objects.filter(employe=search_query_emp)
    else:
        emp = Timesheet.objects.all()

    return render(request, 'timesheet/timesheet_admin.html', {'emp': emp})


def go_timesheet_admin_chant(request):
    timesheet_admin_emp = Timesheet.objects.all()
    search_query_chant = request.GET.get('search_chant', '')

    if search_query_chant:
        chant = Timesheet.objects.filter(chantier=search_query_chant)
    else:
        chant = Timesheet.objects.all()




    return render(request, 'timesheet/timesheet_admin_chantier.html', {'chant': chant})


def go_chantier_admin(request):
    chantier_admin = Chantier.objects.all()

    return render(request, 'timesheet/chantier_admin.html', {'chantier_admin': chantier_admin})


def go_contact(request):
    return render(request, 'timesheet/contact.html')


def go_contact_client(request):
    return render(request, 'timesheet/contact_client.html')



