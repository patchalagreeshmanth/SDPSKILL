from django.db import models

class Admin(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=100,blank=False,unique=True)
    password=models.CharField(max_length=100,blank=False)

    class Meta:
        db_table = "admin_table "

    def _str_(self):
        return self.username

class Course(models.Model):
    id=models.AutoField(primary_key=True)
    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(Honors)"), ("CSIT", "CS&IT")) #tuple format
    department = models.CharField(max_length=20, blank=False,choices=department_choices)
    academic_choices = (("2023-24", "2023-24"), ("2022-23", "2022-23"))
    academicyear = models.CharField(max_length=10, blank=False,choices=academic_choices)
    sem_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=sem_choices)
    Year = models.IntegerField(blank=False)
    coursecode=models.CharField(max_length=20,blank=False)
    coursetitle=models.CharField(max_length=100,blank=False)
    LTPS_struct=models.CharField(max_length=10,blank=False)
    Credit = models.FloatField(blank=False)


    class Meta:
        db_table = "course_table"

    def _str_(self):
        return self.coursecode
class Student(models.Model):
    id=models.AutoField(primary_key=True)
    studentid=models.BigIntegerField(blank=False,unique=True)
    Fullname=models.CharField(max_length=50,blank=False)
    gender_choices = (("Male", "Male"), ("Female", "Female"), ("others", "others"))
    gender=models.CharField(max_length=20,blank=False,choices=gender_choices)
    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(Honors)"), ("CSIT", "CS&IT"))
    department=models.CharField(max_length=50,blank=False,choices=department_choices)
    program_choices = (("BTECH", "BTECH"), ("MTECH", "MTECH"))
    program=models.CharField(max_length=50,blank=False,choices=program_choices)
    sem_choices = (("ODD", "ODD"), ("EVEN", "EVEN"))
    semester = models.CharField(max_length=10, blank=False,choices=sem_choices)
    Year = models.IntegerField(blank=False)
    password=models.CharField(max_length=100,blank=False,default='klu123')
    email=models.CharField(max_length=50,blank=False,unique=True)
    contact=models.CharField(max_length=50,blank=False,unique=True)

    class Meta:
        db_table= "student_table"

    def _str_(self):
        return str(self.studentid)

class Faculty(models.Model):
    id=models.AutoField(primary_key=True)
    facultyid=models.BigIntegerField(blank=False,unique=True)
    Fullname=models.CharField(max_length=50,blank=False)
    gender_choices = (("Male", "Male"), ("Female", "Female"), ("others", "others"))
    gender=models.CharField(max_length=20,blank=False,choices=gender_choices)

    department_choices = (("CSE(R)", "CSE(Regular)"), ("CSE(H)", "CSE(Honors)"), ("CSIT", "CS&IT"),("AIDS", "AI&DS"),("ECEs", "ECE"),("EEEs", "EEE"),("IOTs", "IOT"),("Mech", "ME"),("CIVILs", "CIVIL"))
    department=models.CharField(max_length=50,blank=False,choices=department_choices)

    qualification_choice=(("MTECH","MTECH"),("PH.D", "PH.D"),("MS", "MS"))
    qualification=models.CharField(max_length=50,blank=False,choices=qualification_choice)

    designation_choices = (("prof", "Professor"), ("Assoc.prof", "Associate professor"), ("Asst.prof", "Assitant professor"))
    designation = models.CharField(max_length=50, blank=False,choices=designation_choices)

    password=models.CharField(max_length=100,blank=False,default='klu123')
    email=models.CharField(max_length=50,blank=False,unique=True)
    contact=models.CharField(max_length=50,blank=False,unique=True)

    class Meta:
        db_table= "faculty_table"

    def _str_(self):
        return str(self.Fullname)

class FCourseMappings(models.Model):
            mapid = models.AutoField(primary_key=True)
            Course = models.ForeignKey(Course, on_delete=models.CASCADE)
            faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

            component_choices = (("L","Lecture"),("T","Tutorial"),("P","Practical"),("S","Skilling"))
            component = models.CharField(max_length=10,blank=False,choices=component_choices)

            type=models.BooleanField(blank=False)
            section = models.IntegerField(blank=False)

            class Meta:
                db_table = "fcoursemapp_table"

            def _str_(self):
                return f"{self.Course.coursetitle}-{self.faculty.Fullname}"

