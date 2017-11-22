"""Blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
]

# Використовуйте include() щоб додавати URL з каталогу додатка
from django.conf.urls import include

urlpatterns += [
    url(r'^catalog/', include('catalog.urls')),
]

# Додайте URL співвідношення, щоб перенаправити запити з корневового URL, на URL додатку
from django.views.generic import RedirectView
urlpatterns += [
    url(r'^$', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# Використовуйте static() зоб додавати співвідношення для статичних файлів
# Тільки на період розробки
from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
