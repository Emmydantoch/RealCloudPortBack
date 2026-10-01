from django.test import TestCase
from rest_framework.test import APIClient

from .models import PortfolioProject


class PortfolioProjectListTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        PortfolioProject.objects.create(
            title="Product case study",
            category=PortfolioProject.Category.PRODUCT_DESIGN,
        )
        PortfolioProject.objects.create(
            title="Development project",
            category=PortfolioProject.Category.FULL_STACK_DEVELOPMENT,
        )
        PortfolioProject.objects.create(
            title="Draft project",
            category=PortfolioProject.Category.PRODUCT_DESIGN,
            is_published=False,
        )

    def test_lists_published_projects(self):
        response = self.client.get("/api/projects/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_filters_projects_by_category(self):
        response = self.client.get(
            "/api/projects/",
            {"category": PortfolioProject.Category.PRODUCT_DESIGN},
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            [project["title"] for project in response.data], ["Product case study"]
        )
