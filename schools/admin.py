from django.contrib import admin
from .models import Schools, parent_signup, parents_remark
# Register your models here.


@admin.register(Schools)
class schoolsadmin(admin.ModelAdmin):
	list_display = ('name', 'badge', 'fees', 'video', 'status',  'address')


@admin.register(parent_signup)
class parent_signup (admin.ModelAdmin):
	list_display = ('first_name', 'surname', 'email', 'phone_no')
	fields = ('surname', 'first_name', 'phone_no', 'email')


@admin.register(parents_remark)
class parents_remark(admin.ModelAdmin):
	list_display =('full_name', 'school_name', 'comment')