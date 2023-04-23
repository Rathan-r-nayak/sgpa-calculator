from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from . import models
from django.urls import reverse
from django.template import loader




# Create your views here.
def default(request):
    return render(request,"marksapp/defaultpage.html")

def sgpa(request):
    return render(request,"marksapp/sgpa.html")

def cgpa(request):
    return render(request,"marksapp/cgpa.html")

def cgpaInp(request):
    usn=request.POST["usn"]
    m1=request.POST["sem_cgpa1"]
    m2=request.POST["sem_cgpa2"]
    m3=request.POST["sem_cgpa3"]
    m4=request.POST["sem_cgpa4"]
    m5=request.POST["sem_cgpa5"]
    m6=request.POST["sem_cgpa6"]
    m7=request.POST["sem_cgpa7"]
    m8=request.POST["sem_cgpa8"]
    obj=models.cgpa_db(usn=usn,sem1=m1,sem2=m2,sem3=m3,sem4=m4,sem5=m5,sem6=m6,sem7=m7,sem8=m8)
    obj.save()
    res=cgpaCalc(obj)
    Percentage = (res-0.75)*10
    context={
        "cgpa":res,
        "per":Percentage 
    }
    template=loader.get_template("marksapp/res_cgpa.html")
    return HttpResponse(template.render(context,request))

def cgpaCalc(obj):
    # total=0.0
    # sems=0
    # for i in range(8):
    #     if(obj.sem[i]==None):
    #         continue
    #     else:
    #         total=total+float(obj.sem[i])
    #         sem+=1
    # return total/sems
    return (float(obj.sem1)+float(obj.sem2)+float(obj.sem3)+float(obj.sem4)+float(obj.sem5)+float(obj.sem6)+float(obj.sem7)+float(obj.sem8))/8

def sgpaInp(request):
    sem=request.POST["semester"]
    usn=request.POST["usn"]

    creditName=["sub_credit1","sub_credit2","sub_credit3","sub_credit4","sub_credit5","sub_credit6","sub_credit7","sub_credit8","sub_credit9"]
    credit=[]
    for i in creditName:
        credit.append(int(request.POST[i]))

    marksName=["sub_marks1","sub_marks2","sub_marks3","sub_marks4","sub_marks5","sub_marks6","sub_marks7","sub_marks8","sub_marks9"]
    marks=[]
    for i in marksName:
        marks.append(float(request.POST[i]))

    #marks=list of marks float
    #credit=list of credit int
    res=computeSgpa(marks,credit)
    
    obj=models.sgpa_db(sem=sem,usn=usn,m1=marks[0],m2=marks[1],m3=marks[2],m4=marks[3],m5=marks[4],m6=marks[5],m7=marks[6],m8=marks[7],m9=marks[8],sgpa=res)
    obj.save()

    context={
        "sgpa":res,
    }
    template=loader.get_template("marksapp/res_sgpa.html")
    return HttpResponse(template.render(context,request))


def computeSgpa(marks,credit):
    sgpa=0
    gradept=[]
    for i in range(len(marks)):
        if(marks[i]>=90):
            gradept.append(10)

        elif((marks[i]>=80)&(marks[i]<90)):
            gradept.append(9)

        elif((marks[i]>=70)&(marks[i]<80)):
            gradept.append(8)

        elif((marks[i]>=60)&(marks[i]<70)):
            gradept.append(7)

        elif((marks[i]>=45)&(marks[i]<60)):
            gradept.append(6)

        elif((marks[i]>=40)&(marks[i]<45)):
            gradept.append(4)

        else:
            gradept.append(0)
    totalCrd=0
    crP=0
    for i in range(len(marks)):
        totalCrd+=credit[i]
        crP+=(credit[i]*gradept[i])
    sgpa=crP/totalCrd
    return sgpa