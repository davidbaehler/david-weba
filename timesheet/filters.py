import django_filters
from .models import *
from django_filters import DateFilter

"""https://www.youtube.com/watch?v=yhDJrCJQbfI"""
class TimesheetFilter(django_filters.FilterSet):
    class Meta:
        model = Timesheet
        fields = {
            'date', 'employe', 'chantier'
        }
