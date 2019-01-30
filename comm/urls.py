"""comm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from commapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    url('^home$',views.index),
    url('^signup$',views.insert,name="signin"),
    url('^login$',views.login ),
    url('^search',views.search,name="search"),
    url('^alpha',views.alphabet),
    url('^filter',views.filter_data),
    url('cpass', views.cpassword),
    url('^lg', views.logout),
    url('eprofile',views.editprofile),
    url('event',views.events),
    url('profile',views.myprofile)
    # url('^fpass',views.fpassword),

    # url('^mail',views.massmail)
]
