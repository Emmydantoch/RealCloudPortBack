from rest_framework import serializers

from .models import PortfolioProject


class PortfolioProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = PortfolioProject
        fields = (
            "id",
            "title",
            "category",
            "description",
            "image_url",
            "youtube_url",
            "technologies",
            "project_url",
            "created_at",
        )

    def get_image_url(self, project):
        if not project.image:
            return None

        request = self.context.get("request")
        image_url = project.image.url
        return request.build_absolute_uri(image_url) if request else image_url
