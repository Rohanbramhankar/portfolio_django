from django.contrib import admin
from .models import Project, Contact, Profile, Skill, Education, Experience

admin.site.register(Project)
admin.site.register(Contact)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(Experience)


from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'order', 'is_visible')
    list_editable = ('order', 'is_visible')
