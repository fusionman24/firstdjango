from django.contrib import admin
from .models import User,Startup,PitchRequest

# Register your models here.

print("Registering Admin")

admin.site.register(User)
admin.site.register(Startup)
admin.site.register(PitchRequest)
