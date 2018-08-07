from django.contrib import admin
from .models import Schools, parent_signup
# Register your models here.


@admin.register(Schools)
class schoolsadmin(admin.ModelAdmin):
	list_display = ('School_name', 'school_badge', 'short_video','address')


@admin.register(parent_signup)
class parent_signup (admin.ModelAdmin):
	list_display = ('first_name', 'surname', 'email', 'phone_no')
	fields = ('surname', 'first_name', 'phone_no', 'email')

