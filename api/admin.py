from django.contrib import admin
from .models import User, Run, Pokemon

# Register your models here.
admin.site.register(User)
admin.site.register(Run)
admin.site.register(Pokemon)