from django.db import models


class PortfolioProject(models.Model):
    class Category(models.TextChoices):
        PRODUCT_DESIGN = "product_design", "Product Design"
        FULL_STACK_DEVELOPMENT = "full_stack_development", "Full-stack Development"
        DIGITAL_MARKETING = "digital_marketing", "Digital Marketing"
        GRAPHICS = "graphics", "Graphics"

    title = models.CharField(max_length=160)
    category = models.CharField(max_length=32, choices=Category.choices)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="projects/", blank=True)
    youtube_url = models.URLField(blank=True)
    technologies = models.CharField(max_length=500, blank=True)
    project_url = models.URLField(blank=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
