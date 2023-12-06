from django.contrib import admin
from django.contrib.admin import register
from django.contrib.admin.widgets import FilteredSelectMultiple

from main import models


class UserAdmin(admin.ModelAdmin):
	readonly_fields = ["username"]
	exclude = ["hashed_password"]
	
	# def save_model(self, request, obj, form, change):
	# 	"""is_admin = True == create double in CustomUser else try delete CustomUser"""


@register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
	filter_horizontal = ("videos", "tests")
	save_as = True
	
	def formfield_for_manytomany(self, db_field, request, **kwargs):
		if db_field.name in ["videos", "tests"]:
			kwargs['widget'] = FilteredSelectMultiple(
				db_field.verbose_name, is_stacked=False
			)
		else:
			return super().formfield_for_manytomany(db_field, request, **kwargs)
		form_field = db_field.formfield(**kwargs)
		msg = "Зажмите 'Ctrl' ('Cmd') или проведите мышкой, с зажатой левой кнопкой, чтобы выбрать несколько элементов."
		form_field.help_text = msg
		return form_field


@register(models.Test)
class TopicAdmin(admin.ModelAdmin):
	filter_horizontal = ("topics",)
	save_as = True
	
	def formfield_for_manytomany(self, db_field, request, **kwargs):
		if db_field.name in ["topics"]:
			kwargs['widget'] = FilteredSelectMultiple(
				db_field.verbose_name, is_stacked=False
			)
		else:
			return super().formfield_for_manytomany(db_field, request, **kwargs)
		form_field = db_field.formfield(**kwargs)
		msg = "Зажмите 'Ctrl' ('Cmd') или проведите мышкой, с зажатой левой кнопкой, чтобы выбрать несколько элементов."
		form_field.help_text = msg
		return form_field


admin.site.register(models.SiteUser, UserAdmin)
admin.site.register(models.Textbook)
admin.site.register(models.Video)
