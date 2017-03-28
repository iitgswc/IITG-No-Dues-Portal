from django.template import loader
from models import *
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404, redirect,reverse, HttpResponseRedirect
from django.db.models import Q
from datetime import datetime
from django.db.models.fields import DateTimeField
from django.utils import timezone
from forms import UserForm, LoginForm
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.urls import reverse_lazy
from django.utils.http import is_safe_url
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F

class LoginView(View):
    """
    View class for handling login functionality.
    """
    template_name = 'main/login.html'
    port = 995
    next = ''

    def get(self, request):
        self.next = request.GET.get('next', '')
        if request.user.is_authenticated() and not request.user.is_superuser:
            return redirect('/stud_profile')
        args = dict(form=LoginForm(None), next=self.next)
        return render(request, self.template_name, args)

    def post(self, request):
        redirect_to = request.POST.get('next', self.next)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            server = form.cleaned_data.get('login_server')
            role = form.cleaned_data.get('role')
            print (role)

            user = auth.authenticate(username=username, password=password,
                                     server=server, port=self.port)
            if user is not None :
                if not is_safe_url(url=redirect_to, host=request.get_host()):
                    auth.login(request=request, user=user)
                    if role == "Student":
                        try:
                            student = Student.objects.get(webmail=username)
                        except Student.DoesNotExist:
                            student = None
                        if student is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/stud_profile')
                    elif role == "Faculty":
                        try:
                            fac = Faculty.objects.get(webmail=username)
                        except Faculty.DoesNotExist:
                            fac = None
                        if fac is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/faculty_profile')
                    elif role == "Lab":
                        try:
                            lab = Lab.objects.get(webmail=username)
                        except Faculty.DoesNotExist:
                            lab = None
                        if lab is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/lab_profile')
                    elif role == "Caretaker":
                        try:
                            caretaker = Caretaker.objects.get(webmail=username)
                        except Caretaker.DoesNotExist:
                            caretaker = None
                        if caretaker is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/caretaker_profile')
                    elif role == "Warden":
                        try:
                            warden = Warden.objects.get(webmail=username)
                        except Warden.DoesNotExist:
                            warden = None
                        if warden is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/warden_profile')
                    elif role == "Gymkhana":
                        try:
                            gymnkhana = Gymkhana.objects.get(webmail=username)
                        except Gymkhana.DoesNotExist:
                            gymnkhana = None
                        if gymnkhana is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/gymkhana_profile')
                    elif role == "OnlineCC":
                        try:
                            onlinecc = OnlineCC.objects.get(webmail=username)
                        except OnlineCC.DoesNotExist:
                            onlinecc = None
                        if onlinecc is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/onlinecc_profile')
                    elif role == "CC":
                        try:
                            cc = CC.objects.get(webmail=username)
                        except CC.DoesNotExist:
                            cc = None
                        if cc is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/cc_profile')
                    elif role == "Thesis Manager":
                        try:
                            thesis_manager = SubmitThesis.objects.get(webmail=username)
                        except SubmitThesis.DoesNotExist:
                            thesis_manager = None
                        if thesis_manager is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/thesis_manager_profile')
                    elif role == "Library":
                        try:
                            library = Library.objects.get(webmail=username)
                        except Library.DoesNotExist:
                            library = None
                        if library is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/library_profile')
                    elif role == "Assistant Registrar":
                        try:
                            assistant_registrar = Assistant_registrar.objects.get(webmail=username)
                        except Assistant_registrar.DoesNotExist:
                            assistant_registrar = None
                        if assistant_registrar is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/assireg_profile')
                    elif role == "HOD":
                        try:
                            hod = HOD.objects.get(webmail=username)
                        except HOD.DoesNotExist:
                            hod = None
                        if hod is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/hod_profile')
                    elif role == "Account":
                        try:
                            account = Account.objects.get(webmail=username)
                        except Account.DoesNotExist:
                            account = None
                        if account is None:
                            form.add_error(None, 'Role mismatch')
                            return render(request, self.template_name, dict(form=form))
                        else:
                            return redirect('/account_profile')
                    elif role == "Admin":
                        return redirect('/admin')
                else:
                    return redirect(redirect_to)
            else:
                form.add_error(None, 'No user exists for given credentials.')
                return render(request, self.template_name, dict(form=form))
        else:
            return render(request, self.template_name, dict(form=form))

class LogoutView(LoginRequiredMixin, View):
    """
    View class for handling logout.
    """
    login_url = reverse_lazy('login_user')
    raise_exception = False
    http_method_names = ['get', 'head', 'options']
    def get(self, request):
        auth.logout(request=request)
        return redirect('/')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        print (role)
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #print ('stud1')
                login(request, user)
                #print (role+'1')
                role = str(role)
                #print type(Student.webmail)
                if role == "Student":
                    return redirect('/stud_profile')
                elif role == "Faculty":
                    return redirect('/faculty_profile')
                elif role == "Lab":
                    return redirect('/lab_profile')
                elif role == "Caretaker":
                    return redirect('/caretaker_profile')
                elif role == "Warden":
                    return redirect('/warden_profile')
                elif role == "Gymkhana":
                    return redirect('/gymkhana_profile')
                elif role == "OnlineCC":
                    return redirect('/onlinecc_profile')
                elif role == "CC":
                    return redirect('/cc_profile')
                elif role == "Thesis Manager":
                    return redirect('/thesis_manager_profile')
                elif role == "Library":
                    return redirect('/library_profile')
                elif role == "Assistant Registrar":
                    return redirect('/assireg_profile')
                elif role == "HOD":
                    return redirect('/hod_profile')
                elif role == "Account":
                    return redirect('/account_profile')
                elif role == "Admin":
                    return redirect('/admin')
                else:
                    return render(request, 'main/login.html', {'error_message': 'Unsuccessful Login'})
            else:
                return render(request, 'main/login.html', {'error_message': 'Session Expired'})
        else:
            return render(request, 'main/login.html', {'error_message': 'Credentials Invalid'})
    return render(request, 'main/login.html',{'error_message': ''})

def stud_profile(request):
    username=request.user.username
    student = Student.objects.get(webmail=username)
    return render(request, 'main/stud.html', {'error_message': 'valid login', 'student': student})

def rules(request):
    username=request.user.username
    try:
        student = Student.objects.get(webmail=username)
    except Student.DoesNotExist:
        student = None
    return render(request,'main/rules.html', {'student':student})

def contact(request):
    username = request.user.username
    try:
        student = Student.objects.get(webmail=username)
    except Student.DoesNotExist:
        student = None
    return render(request, 'main/contact.html', {'student': student})

def no_dues_apply(request):
    if request.method == "GET":
        username = request.user.username
        try:
            student = Student.objects.get(webmail=username)
        except Student.DoesNotExist:
            student = None
        if student is None:
            return render(request, 'main/login.html', {'error_message': 'Role mismatch'})
        return render(request, 'main/student_apply.html', {'error_message': 'valid login', 'student': student})
    elif request.method=="POST":
        username = request.user.username
        try:
            student = Student.objects.get(webmail=username)
        except Student.DoesNotExist:
            student = None

        if request.POST.get("library_process_trigger","") == 'on':
            student.library_process_trigger=True
            student.save()
        else :
            student.library_process_trigger=False
            student.submit_thesis= False
            student.submit_thesis_update_time = None
            student.library_approval = False
            student.library_update_time = None
            student.HOD_approval=False
            student.HOD_update_time = None
            student.account_approval=False
            student.account_update_time = None
            student.save()

        if request.POST.get("lab_process_trigger","") == 'on':
            student.lab_process_trigger=True
            student.save()
        else :
            student.lab_process_trigger=False
            lab_approvals = student.get_labs()
            for lab in lab_approvals:
                lab.lab_approval = False
                lab.staus_update_time = None
                lab.save()
            student.HOD_approval = False
            student.HOD_update_time = None
            student.account_approval = False
            student.account_update_time = None
            student.save()

        if request.POST.get("dept_process_trigger","") == 'on':
            if Stud_Faculty_Status.objects.filter(student=student):
                student.dept_process_trigger=True
                student.save()
        else :
            student.dept_process_trigger=False
            fac_approvals = student.get_faculties()
            for fac in fac_approvals :
                fac.faculty_approval = False
                fac.status_update_time = None
                fac.save()
            student.HOD_approval=False
            student.HOD_update_time = None
            student.account_approval=False
            student.account_update_time = None
            student.save()

        if request.POST.get("gymkhana_process_trigger","") == 'on':
            student.gymkhana_process_trigger=True
            student.save()
        else :
            student.gymkhana_process_trigger=False
            student.gymkhana_approval = False
            student.gymkhana_update_time = None
            student.assistant_registrar_approval = False
            student.assistant_registrar_update_time = None
            student.HOD_approval=False
            student.HOD_update_time = None
            student.account_approval=False
            student.account_update_time = None
            student.save()

        if request.POST.get("hostel_process_trigger","") == 'on':
            student.hostel_process_trigger=True
            student.save()
        else :
            student.hostel_process_trigger=False
            student.caretaker_approval = False
            student.caretaker_update_time = None
            student.warden_approval = False
            student.warden_update_time = None
            student.assistant_registrar_approval = False
            student.assistant_registrar_update_time = None
            student.HOD_approval=False
            student.HOD_update_time = None
            student.account_approval=False
            student.account_update_time = None
            student.save()

        if request.POST.get("cc_process_trigger","") == 'on':
            student.cc_process_trigger=True
            student.save()
        else :
            student.cc_process_trigger=False
            student.online_cc_approval = False
            student.online_cc_update_time = None
            student.CC_approval = False
            student.CC_update_time = None
            student.assistant_registrar_approval = False
            student.assistant_registrar_update_time = None
            student.HOD_approval=False
            student.HOD_update_time = None
            student.account_approval=False
            student.account_update_time = None
            student.save()
        return redirect("/no_dues_apply")
        # fix this

def update_faculty_status(request):
    print ("updating lab status")
    stud_webmail = request.GET.get("stud_webmail")
    faculty_webmail = request.GET.get("faculty_webmail")
    student = Student.objects.get(webmail=stud_webmail)
    faculty = Faculty.objects.get(webmail=faculty_webmail)
    x = Stud_Faculty_Status.objects.get(student = student, faculty=faculty)
    x.faculty_approval = not x.faculty_approval
    x.status_update_time = datetime.now()
    x.save()
    if x.faculty_approval is False:
        if student.HOD_approval is True:
            student.HOD_approval = False
            student.HOD_update_time = datetime.now()
        if student.account_approval is True:
            student.account_approval = False
            student.account_update_time = datetime.now()
        student.save()
    return JsonResponse({'messege': "Status updated", 'datetime': x.status_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})

def update_faculty_remarks(request):
    remarks = request.GET.get("remarks")
    stud_roll_no = request.GET.get("stud_roll_no")
    print (stud_roll_no + "1111")
    faculty_webmail = request.GET.get("faculty_webmail")
    student = Student.objects.get(roll_no=stud_roll_no)
    faculty = Faculty.objects.get(webmail=faculty_webmail)
    x = Stud_Faculty_Status.objects.get(student=student, faculty=faculty)
    x.faculty_remarks = remarks
    x.status_update_time = datetime.now()
    x.save()
    return JsonResponse(
        {'messege': "Status updated", 'datetime': x.status_update_time.strftime('%B %d, %Y, %I:%M %p'),
         'webmail': student.webmail})

def update_lab_status(request):
    print ("updating lab status")
    stud_webmail = request.GET.get("stud_webmail")
    lab_webmail = request.GET.get("lab_webmail")
    student = Student.objects.get(webmail=stud_webmail)
    lab = Lab.objects.get(webmail=lab_webmail)
    x = Stud_Lab_Status.objects.get(student = student, lab=lab)
    x.lab_approval = not x.lab_approval
    x.status_update_time = datetime.now()
    x.save()
    if x.lab_approval is False:
        if student.HOD_approval is True:
            student.HOD_approval = False
            student.HOD_update_time = datetime.now()
        if student.account_approval is True:
            student.account_approval = False
            student.account_update_time = datetime.now()
        student.save()
    return JsonResponse({'messege': "Status updated", 'datetime': x.status_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})

def update_lab_remarks(request):
    remarks = request.GET.get("remarks")
    stud_roll_no = request.GET.get("stud_roll_no")
    print (stud_roll_no + "1111")
    lab_webmail = request.GET.get("lab_webmail")
    student = Student.objects.get(roll_no=stud_roll_no)
    lab = Lab.objects.get(webmail=lab_webmail)
    x = Stud_Lab_Status.objects.get(student=student, lab=lab)
    x.lab_remarks = remarks
    x.status_update_time = datetime.now()
    x.save()
    return JsonResponse(
        {'messege': "Status updated", 'datetime': x.status_update_time.strftime('%B %d, %Y, %I:%M %p'),
         'webmail': student.webmail})

def update_status(request):
    print ("reaching")
    status_name = request.GET.get("status_name") #getting name of the attribute
    print (status_name+"1234")
    stud_webmail = request.GET.get("stud_webmail")
    print (stud_webmail + "5678")
    student = Student.objects.get(webmail=stud_webmail)
    status = getattr(student, status_name)
    print (type(status))
    print (status)
    if status_name == 'caretaker_approval':
        print ("inside caretaker")
        student.caretaker_update_time = datetime.now()
        setattr(student, status_name, not status)
        if status is True:
            print ("in the status check")
            if student.warden_approval is True:
                student.warden_approval = False
                student.warden_update_time = datetime.now()
            if student.assistant_registrar_approval is True:
                student.assistant_registrar_approval = False
                student.assistant_registrar_update_time = datetime.now()
            if student.HOD_approval is True:
                student.HOD_approval = False
                student.HOD_update_time = datetime.now()
            if student.account_approval is True:
                student.account_approval = False
                student.account_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.caretaker_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif status_name == 'warden_approval':
        print ("inside warden")
        student.warden_update_time = datetime.now()
        setattr(student, status_name, not status)
        if status is True:
            print ("in the status check")
            if student.assistant_registrar_approval is True:
                student.assistant_registrar_approval = False
                student.assistant_registrar_update_time = datetime.now()
            if student.HOD_approval is True:
                student.HOD_approval = False
                student.HOD_update_time = datetime.now()
            if student.account_approval is True:
                student.account_approval = False
                student.account_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.warden_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif status_name == 'gymkhana_approval':
        print ("inside gymkhana")
        student.gymkhana_update_time = datetime.now()
        setattr(student, status_name, not status)
        if status is True:
            print ("in the status check")
            if student.assistant_registrar_approval is True:
                student.assistant_registrar_approval = False
                student.assistant_registrar_update_time = datetime.now()
            if student.HOD_approval is True:
                student.HOD_approval = False
                student.HOD_update_time = datetime.now()
            if student.account_approval is True:
                student.account_approval = False
                student.account_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.gymkhana_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif status_name == 'assistant_registrar_approval':
        print ("inside assistant_registrar")
        student.assistant_registrar_update_time = datetime.now()
        setattr(student, status_name, not status)
        if status is True:
            print ("in the status check")
            if student.HOD_approval is True:
                student.HOD_approval = False
                student.HOD_update_time = datetime.now()
            if student.account_approval is True:
                student.account_approval = False
                student.account_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.assistant_registrar_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif status_name == 'submit_thesis':
        print (" inside submit_thesis")
        student.submit_thesis_update_time = datetime.now()
        setattr(student, status_name, not status)
        if status is True:
            print ("in the status check")
            if student.library_approval is True:
                student.library_approval = False
                student.library_update_time = datetime.now()
            if student.HOD_approval is True:
                student.HOD_approval = False
                student.HOD_update_time = datetime.now()
            if student.account_approval is True:
                student.account_approval = False
                student.account_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.submit_thesis_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif status_name == 'library_approval':
        print ("inside library")
        student.library_update_time = datetime.now()
        setattr(student, status_name, not status)
        if status is True:
            print "in the status check"
            if student.HOD_approval is True:
                student.HOD_approval = False
                student.HOD_update_time = datetime.now()
            if student.account_approval is True:
                student.account_approval = False
                student.account_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.library_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif status_name == 'online_cc_approval':
        print ("inside online_cc_approval")
        student.online_cc_update_time = datetime.now()
        setattr(student, status_name, not status)
        if status is True:
            print ("in the status check")
            if student.CC_approval is True:
                student.CC_approval = False
                student.CC_update_time = datetime.now()
            if student.HOD_approval is True:
                student.HOD_approval = False
                student.HOD_update_time = datetime.now()
            if student.account_approval is True:
                student.account_approval = False
                student.account_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.online_cc_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif status_name == 'CC_approval':
        print ("inside CC_approval")
        student.CC_update_time = datetime.now()
        setattr(student, status_name, not status)
        if status is True:
            print "in the status check"
            if student.HOD_approval is True:
                student.HOD_approval = False
                student.HOD_update_time = datetime.now()
            if student.account_approval is True:
                student.account_approval = False
                student.account_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.CC_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})

    elif status_name == 'HOD_approval':
        print ("inside HOD")
        student.HOD_update_time = datetime.now()
        setattr(student, status_name, not status)
        if status is True:
            print ("in the status check")
            if student.account_approval is True:
                student.account_approval = False
                student.account_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.HOD_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif status_name == 'account_approval':
        print ("inside account_approval")
        student.CC_update_time = datetime.now()
        setattr(student, status_name, not status)
        if status is True:
            if student.account_approval is True:
                student.account_approval = False
                student.account_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.CC_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})


def update_remarks(request):
    print ("remarks function reaching")
    remarks_name = request.GET.get("remarks_name")  # getting name of the attribute
    remarks = request.GET.get("remarks")
    print (remarks_name + "1234")
    print (remarks + "5678")
    stud_roll_no = request.GET.get("stud_roll_no")
    print (stud_roll_no + "1111")
    student = Student.objects.get(roll_no=stud_roll_no)
    setattr(student, remarks_name, remarks)
    student.save()
    if remarks_name == 'caretaker_remarks':
        print ("inside caretaker remarks")
        student.caretaker_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.caretaker_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif remarks_name == 'warden_remarks':
        print ("inside warden remarks")
        student.warden_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.warden_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif remarks_name == 'gymkhana_remarks':
        print ("inside gymkhana remarks")
        student.gymkhana_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.gymkhana_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif remarks_name == 'assistant_registrar_remarks':
        print ("inside assi_reg remarks")
        student.assistant_registrar_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.assistant_registrar_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif remarks_name == 'library_remarks':
        print ("inside library remarks")
        student.library_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.library_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif remarks_name == 'submit_thesis_remarks':
        print ("inside submit thesis remarks")
        student.submit_thesis_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.submit_thesis_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif remarks_name == 'online_cc_remarks':
        print ("inside online cc remarks")
        student.online_cc_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.online_cc_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif remarks_name == 'cc_remarks':
        print ("inside cc remarks")
        student.CC_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.CC_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif remarks_name == 'hod_remarks':
        print ("inside hod remarks")
        student.HOD_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.HOD_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})
    elif remarks_name == 'account_remarks':
        print ("inside account remarks")
        student.account_update_time = datetime.now()
        student.save()
        return JsonResponse({'messege': "Status updated", 'datetime': student.account_update_time.strftime('%B %d, %Y, %I:%M %p'), 'webmail':student.webmail})

def search_students(request):
    searchquery = request.POST.get("searchquery")
    print (searchquery)
    students = Student.objects.filter(Q(roll_no__icontains=searchquery)|Q(name__icontains=searchquery)|Q(webmail__icontains=searchquery))
    student_details = {}
    for student in students:
        print (student.webmail)
        print (student.name)
        student_details[student.webmail]=student.name
    print (student_details)
    return JsonResponse({'students_searched':student_details})

def add_student(request):
    student_webmail = request.GET.get("student_webmail")
    username = request.user.username
    print (student_webmail+'7777')
    student = Student.objects.get(webmail=student_webmail)
    faculty = Faculty.objects.get(webmail=username)
    print (type(student))
    print (student.webmail+'9999')
    #print type(Stud_Faculty_Status.objects.get(student=student, faculty=fac))
    #print  type(Stud_Faculty_Status(student=student, faculty=fac))
    try:
        x = Stud_Faculty_Status.objects.get(student=student, faculty=faculty)
    except Stud_Faculty_Status.DoesNotExist:
        x = None
    if x is None:
        x = Stud_Faculty_Status(student=student, faculty=faculty)
        print (x.student.webmail+'8888')
        x.save()
        return JsonResponse({'messege' : "Student is added", 'name' : student.name, 'roll_no': student.roll_no, 'webmail':student.webmail, 'dept' :student.department})
    else:
        return JsonResponse({'messege': 'Student was already added', 'name': " "})

def delete_student(request):
    stud_webmail = request.GET.get("stud_webmail")
    faculty_webmail = request.GET.get("faculty_webmail")
    student = Student.objects.get(webmail=stud_webmail)
    faculty = Faculty.objects.get(webmail=faculty_webmail)
    Stud_Faculty_Status.objects.get(student=student, faculty=faculty).delete()
    if not Stud_Faculty_Status.objects.filter(student=student).exists():
        print ("inside faculty")
        student.dept_process_trigger = False
        if student.HOD_approval is True:
            student.HOD_approval = False
            student.HOD_update_time = datetime.now()
        if student.account_approval is True:
            student.account_approval = False
            student.account_update_time = datetime.now()
        student.save()
        print ("student updated")
    return JsonResponse({'messege': 'Student is deleted', 'webmail': stud_webmail})

def search_faculties(request):
    searchquery = request.POST.get("searchquery")
    print (searchquery)
    faculties = Faculty.objects.filter(Q(name__icontains=searchquery)|Q(webmail__icontains=searchquery))
    faculty_details = {}
    for faculty in faculties:
        print (faculty.webmail)
        print (faculty.name)
        faculty_details[faculty.webmail]=faculty.name
    print  (faculty_details)
    return JsonResponse({'faculties_searched':faculty_details})

def add_faculty(request):
    faculty_webmail = request.GET.get("faculty_webmail")
    username = request.user.username
    print (faculty_webmail+'7777')
    student = Student.objects.get(webmail=username)
    fac = Faculty.objects.get(webmail=faculty_webmail)
    print (type(fac))
    print (fac.webmail+'9999')
    #print type(Stud_Faculty_Status.objects.get(student=student, faculty=fac))
    #print  type(Stud_Faculty_Status(student=student, faculty=fac))
    try:
        x = Stud_Faculty_Status.objects.get(student=student, faculty=fac)
    except Stud_Faculty_Status.DoesNotExist:
        x = None
    if x is None:
        x = Stud_Faculty_Status(student=student, faculty=fac)
        print (x.faculty.webmail+'8888')
        x.save()
        return JsonResponse({'messege' : "Faculty is added", 'name' : fac.name, 'status' : x.faculty_approval, 'remarks': x.faculty_remarks})
    else:
        return JsonResponse({'messege': 'Faculty is already added', 'name': " "})

def stud_full_dept(request):
    username = request.user.username
    username=str(username)
    student = Student.objects.get(webmail=username)
    related_faculties = student.get_faculties()
    names = []
    status = []
    remarks = []
    time = []
    for fac in student.faculty_approval.values_list("webmail", flat=True):
        names.append(Faculty.objects.get(webmail=fac).name)
    for fac in related_faculties:
        status.append(fac.faculty_approval)
    for fac in related_faculties:
        remarks.append(fac.faculty_remarks)
    for fac in related_faculties:
        time.append(fac.status_update_time)
    return render(request, 'main/stud_full_dept.html', {'error_message': 'valid login', 'student': student, 'details': zip(names,status, remarks,time)})

def stud_full_lab(request):
    username = request.user.username
    username = str(username)
    student = Student.objects.get(webmail=username)
    labs = student.get_labs()
    names = []
    status = []
    remarks = []
    time = []
    for lab in student.lab_approval.values_list("webmail", flat=True):
        names.append(Lab.objects.get(webmail=lab).name)
    for lab in labs:
        status.append(lab.lab_approval)
    for lab in labs:
        remarks.append(lab.lab_remarks)
    for lab in labs:
        time.append(lab.status_update_time)
    return render(request, 'main/stud_full_lab.html', {'error_message': 'valid login', 'student': student, 'details':zip(names,status,remarks,time)})

def faculty_profile(request):
    if request.method == "GET":
        username = request.user.username
        fac = Faculty.objects.get(webmail=username)
        dept = fac.department
        studs = fac.get_students()
        students = []
        for stud in studs:
            if stud.dept_process_trigger is True:
                students.append(stud)
        status = []
        remarks = []
        update_time = []
        for stud in students:
            status.append(Stud_Faculty_Status.objects.get(faculty = fac, student=stud).faculty_approval)
        for stud in students:
            remarks.append(Stud_Faculty_Status.objects.get(faculty=fac, student=stud).faculty_remarks)
        for stud in students:
            update_time.append(Stud_Faculty_Status.objects.get(faculty=fac, student=stud).status_update_time)

        return render(request, 'main/faculty.html',{'error_message': 'valid login', 'faculty': fac, 'dept': dept,
                                                    'students': zip(students, status, remarks,update_time)})

def lab_profile(request):
    if request.method == "GET":
        username = request.user.username
        lab = Lab.objects.get(webmail=username)
        studs = lab.get_students()
        students = []
        for stud in studs:
            if stud.dept_process_trigger is True:
                students.append(stud)
        status = []
        remarks = []
        update_time = []
        for stud in students:
            status.append(Stud_Lab_Status.objects.get(lab= lab, student=stud).lab_approval)
        for stud in students:
            remarks.append(Stud_Lab_Status.objects.get(lab=lab, student=stud).lab_remarks)
        for stud in students:
            update_time.append(Stud_Lab_Status.objects.get(lab=lab, student=stud).status_update_time)
        return render(request, 'main/lab.html',{'error_message': 'valid login', 'lab': lab,
                                                'students': zip(students, status, remarks, update_time)})

def caretaker_profile(request):
    if request.method == "GET":
        username = request.user.username
        caretaker = Caretaker.objects.get(webmail=username)
        hostel = caretaker.hostel
        students = Student.objects.filter(hostel=hostel, hostel_process_trigger=True)
        return render(request, 'main/caretaker.html',
                      {'error_message': 'valid login', 'students': students, 'caretaker': caretaker, 'hostel': hostel})

def warden_profile(request):
    if request.method == "GET":
        username = request.user.username
        warden = Warden.objects.get(webmail=username)
        hostel = warden.hostel
        students = Student.objects.filter(hostel=hostel, caretaker_approval=True)
        return render(request, 'main/warden.html',
                      {'error_message': 'valid login', 'students': students, 'warden': warden,
                       'hostel': hostel})

def gymkhana_profile(request):
    if request.method == "GET":
        username = request.user.username
        gymnkhana = Gymkhana.objects.get(webmail=username)
        students = Student.objects.filter(gymkhana_process_trigger=True)
        return render(request, 'main/gymkhana.html',
                      {'error_message': 'valid login', 'students': students, 'gymkhana': gymnkhana})

def onlinecc_profile(request):
    if request.method == "GET":
        username = request.user.username
        onlinecc = OnlineCC.objects.get(webmail=username)
        students = Student.objects.filter(cc_process_trigger=True)
        return render(request, 'main/onlinecc.html',
                      {'error_message': 'valid login', 'students': students, 'onlinecc': onlinecc})

def cc_profile(request):
    if request.method == "GET":
        username = request.user.username
        cc = CC.objects.get(webmail=username)
        students = Student.objects.filter(online_cc_approval=True)
        print (students)
        return render(request, 'main/cc.html',
                      {'error_message': 'valid login', 'students': students, 'cc': cc})

def thesis_manager_profile(request):
    if request.method == "GET":
        username = request.user.username
        thesis_manager = SubmitThesis.objects.get(webmail=username)
        students = Student.objects.filter(library_process_trigger=True)
        return render(request, 'main/thesis_manager.html',
                      {'error_message': 'valid login', 'students': students, 'thesis_manager':thesis_manager})

def library_profile(request):
    if request.method == "GET":
        username = request.user.username
        library = Library.objects.get(webmail=username)
        students = Student.objects.filter(submit_thesis=True)
        return render(request, 'main/library.html',
                      {'error_message': 'valid login', 'students': students, 'library': library})

def assireg_profile(request):
    if request.method == "GET":
        username = request.user.username
        assistant_registrar = Assistant_registrar.objects.get(webmail=username)
        students = Student.objects.filter(caretaker_approval=True,warden_approval=True,gymkhana_approval=True)
        return render(request, 'main/assistant_registrar.html',
                      {'error_message': 'valid login', 'students': students, 'assistant_registrar': assistant_registrar})

def hod_profile(request):
    if request.method == "GET":
        username = request.user.username
        hod = HOD.objects.get(webmail=username)
        students = Student.objects.filter(department=hod.department, assistant_registrar_approval=True,
                                          library_approval=True, CC_approval=True)
        return render(request, 'main/hod.html',
                      {'error_message': 'valid login', 'students': students,
                       'hod': hod})

def account_profile(request):
    if request.method == "GET":
        username = request.user.username
        account = Account.objects.get(webmail=username)
        students = Student.objects.filter(HOD_approval=True)
        return render(request, 'main/account.html',
                      {'error_message': 'valid login', 'students': students, 'account': account})

