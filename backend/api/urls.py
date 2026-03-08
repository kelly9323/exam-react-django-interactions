# api/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ListItemViewSet, health_check

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tasks', ListItemViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('health/', health_check),
]
