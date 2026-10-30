from django.contrib import admin

from .models import (
    Project,
    Contact,
    Profile,
    Skill,
    Education,
    Experience,
    Service,
)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "technology", "created_at", "has_demo")
    list_filter = ("category",)
    search_fields = ("title", "description", "technology")
    readonly_fields = ("created_at",)
    fieldsets = (
        (None, {"fields": ("title", "description", "category", "technology")}),
        ("Links", {"fields": ("link", "demo_url")}),
        ("Media", {"fields": ("image", "project_file")}),
        ("Meta", {"fields": ("created_at",)}),
    )

    @admin.display(boolean=True, description="Demo")
    def has_demo(self, obj):
        return bool(obj.demo_url)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at")
    list_editable = ("is_read",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name",)
    search_fields = ("full_name", "hero_description", "summary")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category")
    list_filter = ("category",)
    search_fields = ("name",)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "duration")
    search_fields = ("degree", "institution")


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("role", "company", "duration", "is_internship")
    list_filter = ("is_internship",)
    search_fields = ("role", "company", "description")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "order", "is_visible")
    list_editable = ("order", "is_visible")
    search_fields = ("title", "description")
    list_filter = ("is_visible",)
