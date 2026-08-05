from django.contrib import admin
from .models import Project, Contact, Profile, Skill, Education

admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Education)