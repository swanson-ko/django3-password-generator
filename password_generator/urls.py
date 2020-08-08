"""password_generator URL Configuration

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

from django.urls import path
from generator import views

"""
'eggs' is another path or page

        below with " name='password' " will always look for reference to html file with password
    
    path('generatedpassword/', views.password, name='password'), 
"""

urlpatterns = [
    path('', views.home, name='home'),
    path('password/', views.password, name='password'),
    path('about/', views.about, name='about'),
]
