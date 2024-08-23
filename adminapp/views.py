from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import AddFacultyForm, AddStudentForm
from .models import Admin, Course, Faculty, Student, FCourseMappings


def adminhome(request):
    #adminuname = request.session["auname"]

    return render(request,"adminhome.html")
def logout(request):
    return render(request,"logins.html")

# Create your views here.
def checklogin(request):
    adminuname=request.POST["uname"]
    adminpwd=request.POST["pwd"]

    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=adminpwd))
    print(flag)

    if flag:
        print("Login Success")
        request.session["auname"] = adminuname  #creating a session
        return render(request,"adminhome.html",{"adminuname":adminuname})
        #return HttpResponse("login success")
    else:
        msg="Login Failed"
        return render(request,"logins.html",{"message":msg})
        #return HttpResponse("login failed ")

def checkstudentlogin(request):
    sid=request.POST["sid"]
    pwd=request.POST["pwd"]

    flag=Student.objects.filter(Q(studentid=sid)&Q(password=pwd))
    print(flag)

    if flag:
        print("Login Success")
        request.session["sid"] = sid  #creating a session
        return render(request,"studenthome.html",{"sid":sid})
        #return HttpResponse("login success")
    else:
        msg="Login Failed"
        return render(request,"studentlogin.html",{"message":msg})
        #return HttpResponse("login failed ")

def viewcourses(request):
    courses=Course.objects.all()
    count = Course.objects.count()

    return render(request, "viewcoures.html",{"coursedata":courses,"count":count})

def viewfaculty(request):
    faculty=Faculty.objects.all()
    count = Faculty.objects.count()

    return render(request, "viewfaculty.html",{"facultydata":faculty,"count":count})

def viewstudents(request):
    students = Student.objects.all()
    count=Student.objects.count()
    #adminuname = request.session["auname"]
    return render(request, "viewstudents.html",{"studentdata":students,"count":count})

def adminstudent(request):
    return render(request,"adminstudent.html")
def admincourse(request):

    return render(request,"admincourse.html")
def adminfaculty(request):

    return render(request,"adminfaculty.html")
def addcourse(request):
    return render(request,"addcourse.html")

def updatecourse(request):
    auname = request.session["auname"]
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request,"updatecourse.html",{"adminuname":auname,"courses":courses,"count":count})

def courseupdation(request,cid):
    cid=str(cid)
    return render(request,"courseupdation.html",{"cid":cid})
def courseupdated(request):
    auname = request.session["auname"]
    cid= request.POST["cid"]
    courseid=int(cid)
    ctitle= request.POST["ctitle"]
    ltps=request.POST["ltps"]
    credits=request.POST["credits"]

    Course.objects.filter(id=courseid).update(coursetitle=ctitle,ltps=ltps,credits=credits)
    msg ="Course Updated Successfully"

    return render(request,"courseupdation.html",{"msg":msg,"adminuname":auname,"cid":cid})
def insertcourse(request):
  if request.method=="POST":
    dept=request.POST["dept"]
    year = request.POST["year"]
    Ayear = request.POST["Ayear"]
    semester = request.POST["semester"]
    ccode = request.POST["ccode"]
    ctitle = request.POST["ctitle"]

    course=Course(department=dept,academicyear=Ayear,semester=semester,Year=year,coursecode=ccode,coursetitle=ctitle)

    Course.save(course)
    message = "Course added"
    return render(request,"addcourse.html",{"msg":message})
def deletecourse(request):
    courses = Course.objects.all()
    count = Course.objects.count()
    return render(request, "deletecourse.html", {"coursedata": courses, "count": count})

def cdelete(request,cid):
    Course.objects.filter(id=cid).delete()
    #return HttpResponse("Deleted Successfully")
    return redirect("deletecourse")
def addfaculty(request):

    form=AddFacultyForm()
    if request.method=="POST":
        form1=AddFacultyForm(request.POST)
        if form1.is_valid():
            form1.save()
            #return HttpResponse("Faculty Added")
            message = "Faculty Added"
            return render(request,"addfaculty.html",{"msg":message,"form":form})
        else:
            message = "Faculty Addition Failed"
            return render(request, "addfaculty.html", {"msg": message, "form": form})

    return render(request,"addfaculty.html",{"form":form})

def deletefaculty(request):
    faculty = Faculty.objects.all()
    count = Faculty.objects.count()
    return render(request, "deletefaculty.html", {"facultydata": faculty, "count": count})

def fdelete(request,fid):
    Faculty.objects.filter(id=fid).delete()
    #return HttpResponse("Deleted Successfully")
    return redirect("deletefaculty")

def addstudent(request):

    form=AddStudentForm()
    if request.method=="POST":
        form1=AddStudentForm(request.POST)
        if form1.is_valid():
            form1.save()
            #return HttpResponse("Faculty Added")
            message = "Student Added"
            return render(request,"addstudent.html",{"msg":message,"form":form})
        else:
            message = "Student Addition Failed"
            return render(request,"addstudent.html",{"msg":message,"form":form})


    return render(request,"addstudent.html",{"form":form})
def deletestudent(request):
    student = Student.objects.all()
    count = Student.objects.count()
    return render(request, "deletestudent.html", {"studentdata": student, "count": count})

def studentdelete(request,sid):
    Student.objects.filter(id=sid).delete()
    #return HttpResponse("Deleted Successfully")
    return redirect("deletestudent")

def adminchangepw(request):
    #adminuname = request.session["auname"]
    return render(request,"adminchangepw.html")

def fcoursemapping(request):
    fcourses=FCourseMappings.objects.all()
    print(fcourses)
    #adminuname = request.session["auname"]
    #count = len(fcourses)
    return render(request,"fcoursemapping.html",{"fcourses":fcourses})

def adminupdatepw(request):
    adminuname = request.session["auname"]
    opwd=request.POST["opwd"]
    npwd = request.POST["npwd"]
    print(adminuname,opwd,npwd)

    flag=Admin.objects.filter(Q(username=adminuname)&Q(password=opwd))
    if flag:
        print("old pw is correct")
        Admin.objects.filter(username=adminuname).update(password=npwd)
        print("updated...")
        msg = "password updated"
    else:
        print("old pw is wrong")
        msg = "old password wrong"

    return render(request,"adminchangepw.html",{"adminuname":adminuname,"message":msg})