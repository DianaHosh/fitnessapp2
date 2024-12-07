"""
URL configuration for fitnesssite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from fitnessapp import views
from fitnessapp.views import (
    MealTypeViewSet, WorkoutTypeViewSet, UserViewSet,
    MealViewSet, SleepViewSet, WaterIntakeViewSet, WorkoutViewSet, DailySummaryViewSet
)

router = routers.DefaultRouter()
router.register(r'mealtypes', MealTypeViewSet)
router.register(r'workouttypes', WorkoutTypeViewSet)
router.register(r'users', UserViewSet, basename='user')
router.register(r'meals', MealViewSet)
router.register(r'sleeps', SleepViewSet)
router.register(r'waterintakes', WaterIntakeViewSet)
router.register(r'workouts', WorkoutViewSet)
router.register(r'dailysummary', DailySummaryViewSet)

urlpatterns = [
    path("", views.home, name="home"),
    path("add_meal/", views.add_meal, name="add_meal"),
    path("add_sleep/", views.add_sleep, name="add_sleep"),
    path("add_workout/", views.add_workout, name="add_workout"),
    path("add_water/", views.add_water, name="add_water"),
    path('add_workout_type/', views.add_workout_type, name='add_workout_type'),
    path('add_meal_type/', views.add_meal_type, name='add_meal_type'),

    path('calories_consumed/', views.calories_consumed, name='calories_consumed'),
    path('calories_burned/', views.calories_burned, name='calories_burned'),
    path('sleep_stats/', views.sleep_stats, name='sleep_stats'),
    path('water_intake/', views.water_intake, name='water_intake'),

    path('edit_meal/<int:meal_id>/', views.edit_meal, name='edit_meal'),
    path('delete_meal/<int:meal_id>/', views.delete_meal, name='delete_meal'),

    path('edit_workout/<int:workout_id>/', views.edit_workout, name='edit_workout'),
    path('delete_workout/<int:workout_id>/', views.delete_workout, name='delete_workout'),

    path('edit_sleep/<int:sleep_id>/', views.edit_sleep, name='edit_sleep'),
    path('delete_sleep/<int:sleep_id>/', views.delete_sleep, name='delete_sleep'),

    path('edit_water/<int:water_intake_id>/', views.edit_water, name='edit_water'),
    path('delete_water/<int:water_intake_id>/', views.delete_water, name='delete_water'),

    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/change-password/', views.change_password, name='change_password'),
]
