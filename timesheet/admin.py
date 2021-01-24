from django.contrib import admin
from .models import Chantier
from .models import Timesheet
from .models import Employe
# Register your models here.


admin.site.register(Employe)
admin.site.register(Chantier)
admin.site.register(Timesheet)