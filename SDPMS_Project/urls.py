"""
URL configuration for SDPMS_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include("SDPMS_App.urls")),
    path('forgotpassword/', include("SDPMS_App.urls")),
    path('editableforgotpassword/', include("SDPMS_App.urls")),
    path('otppage/', include("SDPMS_App.urls")),
    path('changepassword/', include("SDPMS_App.urls")),
    path('dashboard/', include("SDPMS_App.urls")),
    path('mentorprofile/', include("SDPMS_App.urls")),
    path('mentorstudentlist/', include("SDPMS_App.urls")),
    path('mentorstudentdetail/', include("SDPMS_App.urls")),
    path('mentorstudentprofile/', include("SDPMS_App.urls")),
    path('mentorstudentselfassessment/', include("SDPMS_App.urls")),
    path('mentorstudentgoalsandchallenges/', include("SDPMS_App.urls")),
    path('mentorstudentachievements/', include("SDPMS_App.urls")),
    path('previousmeeting/', include("SDPMS_App.urls")),
    path('newmeeting/', include("SDPMS_App.urls")),
    path('newmeetingdetails/', include("SDPMS_App.urls")),
    path('newachievement/', include("SDPMS_App.urls")),
    path('editablenewachievement/', include("SDPMS_App.urls")),
    path('mentorstudentpreviousmeeting/', include("SDPMS_App.urls")),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include("SDPMS_App.urls")),
    path('forgotpassword/', include("SDPMS_App.urls")),
    path('editableforgotpassword/', include("SDPMS_App.urls")),
    path('otppage/', include("SDPMS_App.urls")),
    path('changepassword/', include("SDPMS_App.urls")),
    path('dashboard/', include("SDPMS_App.urls")),
    path('studentprofile/', include("SDPMS_App.urls")),
    path('meetingrequest/', include("SDPMS_App.urls")),
    path('selfassessment/', include("SDPMS_App.urls")),
    path('studentachievement/', include("SDPMS_App.urls")),
    path('editableselfassessment/', include("SDPMS_App.urls")),
    path('storingeditableselfassessment/', include("SDPMS_App.urls")),
    path('goalsandchallenges/', include("SDPMS_App.urls")),
    path('previousmeeting/', include("SDPMS_App.urls")),
    path('mentortimetable/', include("SDPMS_App.urls")),
    path('mentorship/', include("SDPMS_App.urls")),
    
]
