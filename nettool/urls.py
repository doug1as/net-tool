"""
URL configuration for nettool project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

# This file is part of the nettool project and contains the URL routing for the application.
# It includes the admin interface and the URLs for the interface_config app.
# The interface_config app is included under the 'interface/' path.
# The admin interface is accessible at 'admin/'.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('interface/', include('interface_config.urls')),
    path('logbook/', include('logbook.urls')),
]
