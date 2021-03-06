"""djangoexp URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from apptwo import views

app_name = 'apptwo'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.sample_view, name = "Home"),
    path('json/', views.sample_json_res, name = "json"),
    path('csv/', views.sample_csv_res, name = "csv"),
    path('',include('apptwo.urls',namespace='apptwo')),
    path("__reload__/", include("django_browser_reload.urls")),
]
