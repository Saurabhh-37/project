"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from apps.demo.views import posts_with_comments

# Initialize the router (if needed for other views)
router = routers.DefaultRouter()

# Add the path to your new API endpoint
urlpatterns = [
    path('', include(router.urls)),  # Default router URLs
    path('posts/', posts_with_comments, name='posts_with_comments'),  # New endpoint for posts with comments
]
