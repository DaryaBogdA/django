from django.contrib import admin
from .models import Style, Teacher, Price, UserProfile


admin.site.register(Style)
admin.site.register(Teacher)
admin.site.register(Price)
admin.site.register(UserProfile)