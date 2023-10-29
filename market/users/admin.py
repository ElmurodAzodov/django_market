from django.contrib import admin
from .models import CustomUser, Saved


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Saved)