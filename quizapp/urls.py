from . import views
from django.urls import path

urlpatterns=[
    path('',views.index,name='index'),
    path('login/',views.loginuser,name='login'),
    path('teacherregister/',views.teacherregister,name='teacherregister'),
    path('studentregister/',views.studentregister,name='studentregister'),
    path('teacherlogout/',views.teacherlogout,name='teacherlogout'),
    path('selectquiz/',views.selectquiz,name='selectquiz'),
    path('selectobjective/',views.selectobjective,name='selectobjective'),
    path('AddQuestion/',views.AddQuestion,name='AddQuestion'),
    path('MCQsForm/',views.MCQsForm,name='MCQsForm'),
    # path('booked/',views.booked,name='boooked'),
    path('QuizConstraints/',views.QuizConstraints,name='QuizConstraints'),
    path('TeacherFeedback/',views.TeacherFeedback,name='TeacherFeedback'),
    path('StudentInfo/',views.StudentInfo,name='StudentInfo'),
    path('StudentMCQForm/',views.StudentMCQForm,name='StudentMCQForm'),
    path('newdata/',views.newdata,name='newdata'),
    path('TeacherShowResult/',views.TeacherShowResult,name='TeacherShowResult'),
    path('ViewResult/',views.ViewResult,name='ViewResult'),
    
]