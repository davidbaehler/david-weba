from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from timesheet import views



urlpatterns = [
    path('', views.go_index, name='go_index'),
    path('index.html', views.go_index, name='go_index'),
    path('login.html', views.go_connexion, name='go_connexion'),
    path('logged_out.html', views.go_deconnexion, name='go_deconnexion'),
    path('client_accueil.html', views.go_accueil_client, name='go_accueil_client'),
    path('employe_accueil.html', views.go_accueil_employe, name='go_accueil_employe'),
    path('admin_accueil.html', views.go_accueil_admin, name='go_accueil_admin'),
    path('login_success', views.login_success, name='login_success'),
    path('consulter_timesheet.html', views.go_timesheet_emp, name='go_timesheet_emp'),
    path('timesheet_admin.html', views.go_timesheet_admin, name='go_timesheet_admin'),
    path('chantier_admin.html', views.go_chantier_admin, name='go_chantier_admin'),
    path('contact.html', views.go_contact, name='go_contact'),
    path('contact_client.html', views.go_contact_client, name='go_contact_client'),
    path('timesheet_admin_emp.html', views.go_emp_ts,name='go_emp_ts'),
    path('timesheet_admin_chantier.html', views.go_timesheet_admin_chant,name='go_timesheet_admin_chant')
]