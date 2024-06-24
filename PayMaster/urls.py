"""
URL configuration for PayMaster project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import include, path  # type: ignore
from django.conf.urls.static import static  # type: ignore
from . import settings
from . import views
from rest_framework.documentation import include_docs_urls # type: ignore



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePrincipal,name='homeGeneral'),
    path('menu', views.menu,name='menu'),

    path("independientes/", include ('Independientes.urls')),
    path("empresarial/", include ('Empresarial.urls')),
    path('docs/',include_docs_urls(title='Documentation REST Independiente')),
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
