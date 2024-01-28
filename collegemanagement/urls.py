from college import views
"""
URL configuration for collegemanagement project.

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
from django.contrib import admin
from django.urls import path,include
from .views import DashboardView

app_name=''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.adminclick_view,name=''),
    path("", DashboardView.as_view(), name="dashboard"),


    path('aboutus',views.about_view),
    path('contactus',views.contact_view),

    path('adminclick',views.adminclick_view,name='adminclick'),
    path('staffclick',views.staffclick_view),
    path('studentclick',views.studentclick_view),

    path('signup',views.student_signup,name='signup'),
    path('signin',views.student_signin,name='signin'),

    path('',include("event.urls")),
    path('accounts',include("accounts.urls")),

]
