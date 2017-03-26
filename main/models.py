

from django.db import models
from constants import GENDER, DEPARTMENT, PROGRAMMES
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext as _


class Faculty(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    #availability = models.BooleanField(default=True)
    department = models.CharField(max_length=250, blank=True)

    #getting all students related to faculty
    def get_students(self):
        students = []
        for stud in Stud_Faculty_Status.objects.filter(faculty=Faculty.objects.get(webmail=self.webmail)):
            students.append(stud.student)
        return students

    def __str__(self):
        return self.name

class Lab(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)

    #getting all the students related to the lab
    def get_students(self):
        #lab_approvals = self.lab_approval.values_list("webmail", flat=True)
        students = []
        for stud in Stud_Lab_Status.objects.filter(lab=Lab.objects.get(webmail=self.webmail)):
            students.append(stud.student)
        return students

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    roll_no = models.IntegerField(default=0)
    hostel = models.CharField(max_length=250, blank=True)
    department = models.CharField(max_length=250,blank=True)

    faculty_approval = models.ManyToManyField(Faculty, through='Stud_Faculty_Status')
    lab_approval = models.ManyToManyField(Lab, through= 'Stud_Lab_Status')
    caretaker_approval  = models.BooleanField(default=False)
    warden_approval = models.BooleanField(default=False)
    gymkhana_approval = models.BooleanField(default=False)
    HOD_approval = models.BooleanField(default=False)
    assistant_registrar_approval = models.BooleanField(default=False)
    CC_approval = models.BooleanField(default=False)
    library_approval = models.BooleanField(default=False)
    account_approval = models.BooleanField(default=False)
    online_cc_approval = models.BooleanField(default=False)
    submit_thesis = models.BooleanField(default=False)

    caretaker_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    warden_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    assistant_registrar_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True  )
    gymkhana_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True  )
    CC_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True  )
    online_cc_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True  )
    submit_thesis_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True  )
    library_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True  )
    HOD_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True  )
    account_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True  )
    dept_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True  )
    lab_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True  )

    #Process Triggers, activated by student
    library_process_trigger = models.BooleanField(default=False)
    dept_process_trigger = models.BooleanField(default=False)
    lab_process_trigger = models.BooleanField(default=False)
    gymkhana_process_trigger = models.BooleanField(default=False)
    hostel_process_trigger = models.BooleanField(default=False)
    cc_process_trigger = models.BooleanField(default=False)

    #Remarks text
    caretaker_remarks = models.CharField(max_length=1000, blank=True)
    warden_remarks = models.CharField(max_length=1000, blank=True)
    gymkhana_remarks = models.CharField(max_length=1000, blank=True)
    assistant_registrar_remarks = models.CharField(max_length=1000, blank=True)
    cc_remarks = models.CharField(max_length=1000, blank=True)
    online_cc_remarks = models.CharField(max_length=1000, blank=True)
    submit_thesis_remarks = models.CharField(max_length=1000, blank=True)
    library_remarks = models.CharField(max_length=1000, blank=True)
    hod_remarks = models.CharField(max_length=1000, blank=True)
    account_remarks = models.CharField(max_length=1000, blank=True)

    def dept_status(self):
        #faculty_dept=Faculty.objects.filter(department=self.department)
        if Stud_Faculty_Status.objects.filter(student=self):
            dept_status = True
            for fac in self.get_faculties():
                status = fac.faculty_approval
                if status is False:
                    dept_status = False
                    break
            return dept_status
        else:
            return False

    def lab_status(self):
        #labs=Lab.objects.all()
        lab_status = True
        for lab in self.get_labs():
            status = lab.lab_approval
            if status is False:
                lab_status = False
                break
        return lab_status

    #getting faculties related to the student
    def get_faculties(self):
        fac_approvals = self.faculty_approval.values_list("webmail", flat=True)
        faculties = []
        for fac in fac_approvals:
            x = Stud_Faculty_Status.objects.get(faculty=Faculty.objects.get(webmail=fac), student=self)
            faculties.append(x)
        return faculties


    #getting the labs related to the student
    def get_labs(self):
        lab_approvals = self.lab_approval.values_list("webmail", flat=True)
        labs = []
        for lab in lab_approvals:
            x = Stud_Lab_Status.objects.get(lab=Lab.objects.get(webmail=lab), student=self)
            labs.append(x)
        return labs

    def __str__(self):
        return self.name

class Stud_Faculty_Status(models.Model):
    faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    faculty_approval = models.BooleanField(default = False)
    faculty_remarks= models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.student.name


class Stud_Lab_Status(models.Model):
    lab = models.ForeignKey(Lab,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    status_update_time = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    lab_remarks = models.CharField(max_length=1000, blank=True)
    lab_approval = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name


class Caretaker(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    hostel = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return self.name

class Warden(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    hostel = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.name

class Assistant_registrar(models.Model):
    name = models.CharField(max_length=250, default='Assi. Registrar')
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    def __str__(self):
        return self.name

class HOD(models.Model):
    name = models.CharField(max_length=250, blank=True)
    webmail = models.CharField(max_length=250, unique=True, blank=True)
    department = models.CharField(max_length=250,blank=True)
    def __str__(self):
        return self.name

class CC(models.Model):
    name = models.CharField(max_length=250, default='Computer Center')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    def __str__(self):
        return self.name

class Library(models.Model):
    name = models.CharField(max_length=250, default='Library')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    def __str__(self):
        return self.name

class Gymkhana(models.Model):
    name = models.CharField(max_length=250, default='Gymkhana')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    def __str__(self):
        return self.name

class OnlineCC(models.Model):
    name = models.CharField(max_length=250, default='OnlineCC Manager')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    def __str__(self):
        return self.name

class SubmitThesis(models.Model):
    name = models.CharField(max_length=250, default='Thesis Manager')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    def __str__(self):
        return self.name

class Account(models.Model):
    name = models.CharField(max_length=250, default='Account')
    webmail = models.CharField(max_length=250, unique=True,blank=True)
    def __str__(self):
        return self.name