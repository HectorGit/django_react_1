"""dashboardproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from core.views import front

from core.views import front, note, note_detail #https://dev.to/nagatodev/how-to-connect-django-to-reactjs-part-2-2oje


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", front, name="front"), #following the tutorial : https://dev.to/nagatodev/how-to-connect-django-to-reactjs-1a71
    path("notes/", note, name="note"), #https://dev.to/nagatodev/how-to-connect-django-to-reactjs-part-2-2oje
    path("notes/<int:pk>/", note_detail, name="detail"), #https://dev.to/nagatodev/how-to-connect-django-to-reactjs-part-2-2oje
]
