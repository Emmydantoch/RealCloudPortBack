from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from .models import PortfolioProject
from .serializers import PortfolioProjectSerializer


class PortfolioProjectListView(ListAPIView):
    serializer_class = PortfolioProjectSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        projects = PortfolioProject.objects.filter(is_published=True)
        category = self.request.query_params.get("category")
        if category:
            projects = projects.filter(category=category)
        return projects
