from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import *

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.
import random

def index(request):
    return render(request,'index.html')

def loginuser(request):
    if request.method=='POST':
        if request.POST.get('LT'):
            if request.user.is_authenticated:
                return redirect('selectquiz')
            else:
                if request.method == 'POST':
                    username = request.POST.get('username')
                    password =request.POST.get('password')

                    user = authenticate(request, username=username, password=password)

                    if user is not None:
                        login(request, user)
                        return redirect('selectquiz')
                    else:
                        messages.info(request, 'Username OR password is incorrect')
        else:
            if request.user.is_authenticated:
                userid=request.user.id
                student=StudentData.objects.get(id=userid)
                student_username=student.name             #student ke andr pori row hai jiska roll no hai
                dat_rollno=student.rollno  
                context={'su':student_username,'rollno':dat_rollno}
                return render(request,'StudentInfo.html',context)
            else:
                if request.method == 'POST':
                    rollno = request.POST.get('username')
                    password =request.POST.get('password')
                    # print(rollno,password)
                    try:
                        student=StudentData.objects.get(rollno=rollno)
                        student_username=student.name             #student ke andr pori row hai jiska roll no hai
                        dat_rollno=student.rollno   
                        dat_password=student.password
                        # print("s",student_username,dat_rollno,dat_password)
                        # print(dat_password,dat_rollno)
                        if dat_rollno==rollno and dat_password==password:
                            print("Successful")
                            context={'su':student_username,'rollno':dat_rollno}
                            # return redirect('StudentInfo')
                            return render(request,'StudentInfo.html',context)
                            # print(student.id)
                        # if user is not None:
                            # login(request,student.username)
                            # context={'su':student_username,'sr':dat_rollno}  #html mai data behajna hai
                            # return render(request,'portal/studentinfo.html',context)
                        else:
                            messages.info(request, 'Username OR password is incorrect')
                    except Exception as error:
                        print(error)

    context = {}
    return render(request,'teacherlogin.html')
def teacherlogout(request):
    logout(request)
    return redirect('login')
def teacherregister(request):
    form=CreateUserForm()

    if request.method=="POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            print("Successful")
            return redirect("teacherteacherlogin") 
    context={'form':form}
    
    return render(request,'teacherregister.html',context)

# @login_required(login_url='teacherlogin')
def selectquiz(request):
    return render(request,'selectquiz.html')
# @login_required(login_url='teacherlogin')
def selectobjective(request):
    return render(request,'selectobjective.html')


# @login_required(login_url='teacherlogin')
def AddQuestion(request):
    if request.method=='POST':
        ### if name:
        if request.method == 'POST' and request.POST.get("addmore"):
        # quizcode=request.POST.get("quizcode")
            data=QuizCode.objects.last()
            quizcode=data.quizcode
            QUES=request.POST.get("QUES")
            C1=request.POST.get("C1")
            W1=request.POST.get("option1")
            W2=request.POST.get("option2")
            W3=request.POST.get("option3")
            W4=request.POST.get("option4")
            print(QUES, C1, W1, W2, W3,W4)
            obj=QuizData.objects.create(question=QUES, correctansw=C1, wrongansw1=W1, wrongansw2=W2, wrongansw3=W3,wrongansw4=W4, qquizcode=quizcode)  
            obj.save()
        else:
            data=QuizCode.objects.last()
            quizcode=data.quizcode
            QUES=request.POST.get("QUES")
            C1=request.POST.get("C1")
            W1=request.POST.get("option1")
            W2=request.POST.get("option2")
            W3=request.POST.get("option3")
            W4=request.POST.get("option4")
            print(QUES, C1, W1, W2, W3)
            obj=QuizData.objects.create(question=QUES, correctansw=C1, wrongansw1=W1, wrongansw2=W2, wrongansw3=W3,wrongansw4=W4, qquizcode=quizcode) 
            # obj=corectoption.objects.create(question=QUES, correctansw=C1)  
            obj.save()
            return redirect('MCQsForm')
    return render(request,'AddQuestionMCQ.html')
    

# @login_required(login_url='teacherlogin')
def MCQsForm(request):
    data1=QuizCode.objects.last()
    quizcode=data1.quizcode
    alldata=QuizData.objects.filter(qquizcode=quizcode) #last quiz code ka sara data ajai ga alldata mai filter h0ke
    # print(alldata)
    alldatas=list(alldata)
    print(alldatas)
    context={'alldatas':alldatas}





    return render(request,'MCQsForm.html',context)

# @login_required(login_url='teacherlogin')
def QuizConstraints(request):
    if request.method=='POST':
        quizcode=request.POST.get("quizcode")
        if quizcode:
            userid=request.user.id
            print(quizcode,userid)
            obj=QuizCode.objects.create(userid=userid,quizcode=quizcode)  
            obj.save()
            return redirect('AddQuestion')
        else:
            messages.info(request, 'Enter Quizcode')
    return render(request,'QuizConstraints.html')    

def TeacherFeedback(request):
    return render(request,'TeacherFeedback.html')   

def studentregister(request):
    if request.method=='POST' and request.POST.get("password")==request.POST.get("confirmpassword"):
        username=request.POST.get("name")
        rollno=request.POST.get("rollno")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")
        print(username,rollno,password,confirmpassword)
        obj=StudentData.objects.create(name=username,rollno=rollno,password=password,confirmpassword=confirmpassword)
        obj.save()
    else:
        messages.info(request, 'Both password doesnot match')
    return render(request,'studentregister.html')   


def StudentInfo(request):    #student info save karany ke liye for attemting quiz(quiz code)
    if request.method == 'POST':
        name=request.POST.get('name')
        rollno=request.POST.get('rollno')
        quizcodes=request.POST.get('quizcode')
        print(name,rollno,quizcodes)
        obj=MCQAttemptStudent.objects.create(name=name,rollno=rollno,quizcode=quizcodes) #model ka cloumn hai jo orange se likha hai aur white wala hamara data hai
        obj.save()
        # data1=QuizCode.objects.last()
        # quizcode=data1.quizcode
        alldata=QuizData.objects.filter(qquizcode=quizcodes) #last quiz code ka sara data ajai ga alldata mai filter h0ke
        # print(alldata)
        alldatas=list(alldata)
        print(alldatas)
        context={'alldatas':alldatas,'rollno':rollno}
        return render(request,'MCQsFormStudent.html',context) 





    # return render(request,'MCQsForm.html',context)
        # return redirect('StudentMCQForm')
        # lst=list(request.POST)

    # form = SudentInfoDataForm()
    # context ={'forms': form}
    return render(request,'StudentInfo.html') 

def StudentMCQForm(request):
    print(request.user.id)
    return render(request,'MCQsFormStudent.html') 

def newdata(request):
    if request.method=="POST":
        # print(request.POST)
        # print(request.POST)
        # print(request.user.id)
        rollnos=request.POST.get("rollno")
        # print("SA",did)
        # sdata=StudentData.objects.get(id=did)
        # sdata=sdata.rollno
        # print(sdata)
        new=request.POST.dict()   #list mai convert kara hai
        news=list(new.items())
        news=news[2::]
        print(news)
        lengthh=len(news)
        qdata=news[0][0]
        print("qdata",qdata)
        quizd=QuizData.objects.get(id=qdata)
        print(quizd.qquizcode)
        # print(news)
        # id=news[0][0]
        totals_marks=0
        for i in range(len(news)):
            userquestionid=news[i][0]
            useroption=news[i][1]
            answer=QuizData.objects.get(id=userquestionid)
            # print(answer.correctansw)
            if useroption==answer.correctansw:
                totals_marks=totals_marks+1
        # print(totals_marks)
        total=str(totals_marks) + '/' + str(lengthh)
        print(total)
        student=StudentMarks.objects.create(rollno=rollnos,marks=total,quizcode=quizd.qquizcode)
        context={'totals_marks':total}
        return render(request,'QuizFeedbackStudent.html',context)




    return render(request,'QuizFeedbackStudent.html') 

def TeacherShowResult(request):
    # print(request.user.id)
    return render(request,'TeacherShowResult.html')

def ViewResult(request):
    # print(request.user.id)
    # print(request.POST.get('quizcode'))  #quizcode ka data aiga ismai
    if request.method == 'POST':
        quizcodee=request.POST.get('quizcode')
        quizdata=StudentMarks.objects.filter(quizcode=quizcodee)
        print(quizdata)


    return render(request,'ViewResult.html')

