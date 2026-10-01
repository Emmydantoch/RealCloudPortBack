from django.urls import path

from .views import PortfolioProjectListView

urlpatterns = [
    path("projects/", PortfolioProjectListView.as_view(), name="project-list"),
]
