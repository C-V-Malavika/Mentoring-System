from django.urls import include,path
from . import views

urlpatterns = [
    path('login/',views.login,name="login"),
    path('forgotpassword/',views.forgotpassword,name="forgotpassword"),
    path('editableforgotpassword/',views.editableforgotpassword,name="editableforgotpassword"),
    path('otppage/',views.otppage,name="otppage"),
    path('changepassword/',views.changepassword,name="changepassword"),
    path('mentorstudentlist/',views.mentorstudentlist,name="mentorstudentlist"),
    path('mentorstudentdetails/',views.mentorstudentdetails,name="mentorstudentdetails"),
    path('mentorstudentprofile/',views.mentorstudentprofile,name="mentorstudentprofile"),
    path('mentorstudentselfassessment/',views.mentorstudentselfassessment,name="mentorstudentselfassessment"),
    path('mentorstudentgoalsandchallenges/',views.mentorstudentgoalsandchallenges,name="mentorstudentgoalsandchallenges"),
    path('editablementorstudentgoalsandchallenges/',views.editablementorstudentgoalsandchallenges,name="editablementorstudentgoalsandchallenges"),
    path('storingeditablementorstudentgoalsandchallenges/',views.storingeditablementorstudentgoalsandchallenges,name="storingeditablementorstudentgoalsandchallenges"),
    path('mentorstudentachievements/',views.mentorstudentachievements,name="mentorstudentachievements"),
    path('mentorstudentpreviousmeeting/',views.mentorstudentpreviousmeeting,name="mentorstudentpreviousmeeting"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('studentprofile/',views.studentprofile,name="studentprofile"),
    path('meetingrequest/',views.meetingrequest,name="meetingrequest"),
    path('editablemeetingrequest/',views.editablemeetingrequest,name="editablemeetingrequest"),
    path('selfassessment/',views.selfassessment,name="selfassessment"),
    path('studentachievement/',views.studentachievement,name="studentachievement"),
    path('editableselfassessment/',views.editableselfassessment,name="editableselfassessment"),
    path('storingeditableselfassessment/',views.storingeditableselfassessment,name="storingeditableselfassessment"),
    path('goalsandchallenges/',views.goalsandchallenges,name="goalsandchallenges"),
    path('newmeeting/',views.newmeeting,name="newmeeting"),
    path('newachievement/',views.newachievement,name="newachievement"),
    path('editablenewachievement/',views.editablenewachievement,name="editablenewachievement"),
    path('newmeetingdetails/',views.newmeetingdetails,name="newmeetingdetails"),
    path('previousmeeting/',views.previousmeeting,name="previousmeeting"),
    path('mentortimetable/',views.mentortimetable,name="mentortimetable"),
    path('mentorprofile/',views.mentorprofile,name="mentorprofile"),
    path('mentorship/',views.mentorship,name="mentorship"),  
]
    