from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MealView
router = DefaultRouter()
router.register('meals', MealView, basename='meal')


urlpatterns = [
    path('api/', include(router.urls)),
]