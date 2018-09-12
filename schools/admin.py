from django.contrib import admin
from .models import Schools, parents_remark, school_data, profile
# Register your models here.


@admin.register(Schools)
class schoolsadmin(admin.ModelAdmin):
	list_display = ('name', 'badge', 'fees_range', 'video', 'status',  'address')

@admin.register(profile)
class profile(admin.ModelAdmin):
	list_display = ('title', 'first_name', 'surname', 'email')

@admin.register(school_data)
class school_data(admin.ModelAdmin):
	list_display = ('date_established', 'curriculum', 'website', 'awards')

@admin.register(parents_remark)
class parents_remark(admin.ModelAdmin):
	list_display =('full_name', 'school_name', 'comment')