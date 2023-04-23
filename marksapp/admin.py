from django.contrib import admin
from marksapp.models import cgpa_db
from marksapp.models import sgpa_db


# Register your models here.
admin.site.register(cgpa_db)
admin.site.register(sgpa_db)