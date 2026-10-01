from django.contrib import admin

from .models import PortfolioProject


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_published", "created_at")
    list_filter = ("category", "is_published")
    search_fields = ("title", "description", "technologies")
    fields = (
        "title",
        "category",
        "description",
        "image",
        "youtube_url",
        "technologies",
        "project_url",
        "is_published",
    )
