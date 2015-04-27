from django.contrib import admin
import core.models as coremodels
from core.models import UserProfile

# Register your models here.

admin.site.register(coremodels.Location)
admin.site.register(coremodels.Review)
admin.site.register(UserProfile)