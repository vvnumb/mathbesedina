from django.contrib import admin
from main.models import SiteUser, Topic, Textbook

admin.site.register(SiteUser)
admin.site.register(Textbook)
admin.site.register(Topic)
