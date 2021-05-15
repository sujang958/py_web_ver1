"""s1te URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from s1te.views import *
from bookmark.views import *
from django.conf.urls.static import static
from django.conf import settings
import blog.views as blogViews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),

    path('bookmark/', BookmarkLV.as_view(), name="bookmark_index"),
    path('bookmark/create', BookmarkCV.as_view(), name="bookmark_create"),
    path('bookmark/update/<pk>', BookmarkUV.as_view(), name="bookmark_update"),
    path('bookmark/delete/<pk>', BookmarkRV.as_view(), name="bookmark_delete"),
    path('bookmark/<pk>', BookmarkDV.as_view()),

    path('about/', AboutView.as_view()),
    path('blog/', blogViews.BlogLV.as_view(), name='blog'),

    path('accounts/register/', UserCreateView.as_view(), name="register"),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name="register_done"),
    path('accounts/', include('django.contrib.auth.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)