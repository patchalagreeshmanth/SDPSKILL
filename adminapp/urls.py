from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
    path("adminhome",views.adminhome,name="adminhome" ),
    path("logout",views.logout,name="logout"),
    path("checklogin",views.checklogin,name="checklogin"),

    path("viewcourses", views.viewcourses, name="viewcourses"),
    path("viewfaculty", views.viewfaculty, name="viewfaculty"),
    path("viewstudents", views.viewstudents, name="viewstudents"),

    path("admincourse",views.admincourse,name="admincourse" ),
    path("adminfaculty",views.adminfaculty,name="adminfaculty" ),
    path("adminstudent",views.adminstudent,name="adminstudent" ),

    path("addcourse",views.addcourse,name="addcourse" ),
    path("insertcourse", views.insertcourse, name="insertcourse"),
    path("deletecourse",views.deletecourse,name="deletecourse" ),
    path("cdelete/<int:cid>", views.cdelete, name="cdelete"),
    path("updatecourse",views.updatecourse,name="updatecourse"),
    path("courseupdation/<int:cid>",views.courseupdation,name="courseupdation"),
    path("courseupdated",views.courseupdated,name="courseupdated"),

    path("addfaculty",views.addfaculty,name="addfaculty" ),
    path("deletefaculty",views.deletefaculty,name="deletefaculty" ),
    path("fdelete/<int:fid>", views.fdelete, name="fdelete"),
    path("fcoursemapping", views.fcoursemapping, name="fcoursemapping"),

    path("addstudent",views.addstudent,name="addstudent" ),
    path("deletestudent", views.deletestudent, name="deletestudent"),
    path("studentdelete/<int:sid>", views.studentdelete, name="studentdelete"),

    path("adminchangepw", views.adminchangepw, name="adminchangepw"),
    path("adminupdatepw", views.adminupdatepw, name="adminupdatepw"),

]
