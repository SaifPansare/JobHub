
from django.conf import settings
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Employer, Jobs, JobSeeker, Applicant
from django.core.mail import send_mail, EmailMessage





def home(request):
    job = Jobs.objects.all()
    return render(request, 'home.html', {'job': job})






def signup(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        #print("hello", role)
        if role == "Employer":
            return render(request, 'EmployerSignup.html', {})
        else:
            return render(request, 'JobSeekerSignup.html', {})
           
    
    return render(request, 'checkEmployeerOrJobseeker.html', {})






def signup_employer(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        job = Jobs.objects.all()

        
        if name and email and password and role:
            signUp = Employer(username=name,
                              email=email,
                              password=password,
                              role=role)
            signUp.save()
            return render(request, 'employeer.html', {'name': name,
                                                          'jobs': job,})





def signup_job_seeker(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
                
        if name and email and password and role:
            signUp = JobSeeker(username=name,
                               email=email,
                               password=password,
                               role=role)
            signUp.save()
            jobs = Jobs.objects.all()
            return render(request, 'JobSeeker.html', {'name': name,'job': jobs})





def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        
        if name and password:
            jobs = Jobs.objects.all()
            try:
                emp = Employer.objects.get(username=name)
                #print("hello",emp.username)
                if emp:
                    emp_id = emp.employer_id
                    if password == emp.password:
                        if emp.role == "Employeer":
                            return render(request, 'employeer.html', {'emp_id': emp_id,
                                                                      'jobs': jobs,
                                                                      'name': name,})
                else:
                    return HttpResponse('Enter correct credentials') 
            except Exception as e:
                js = JobSeeker.objects.get(username = name)
                #print("hello",js.username)
                if js:
                    if password == js.password:
                        return render(request, 'Jobseeker.html', {'name': name,
                                                              'job': jobs,})
                    else:
                        return HttpResponse('Enter correct credentials')    
                  
    return render(request, 'login.html', {})




def add_job(request, emp_name):
    if request.method == "POST":
        job_role = request.POST.get('job_role')
        company = request.POST.get('company')
        salary = request.POST.get('salary')
        description = request.POST.get('description')

        if job_role and company and salary:
            emp = Employer.objects.get(username = emp_name)
            emp_id = emp.employer_id
            job = Jobs(job_role=job_role,
                        company=company,
                        salary=salary,
                        description = description,
                        employer=emp)
            job.save()
            jobs = Jobs.objects.all()
            return render(request, 'employeer.html', {'emp_id': emp_id,
                                                      'jobs': jobs,})
        else:
            return render(request, 'add_job.html', {'name': emp_name})        

    return render(request, 'add_job.html', {'name': emp_name})






def del_job(request, job_id):
    job = Jobs.objects.get(pk = job_id)
    name = job.employer.username
    emp_id = job.employer.employer_id
    job.delete()
    jobs = Jobs.objects.all()
    return render(request, 'employeer.html', {'name': name,
                                              'jobs': jobs,
                                              'emp_id': emp_id,})    





def job_apply(request, job_id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        resume_file = request.FILES.get('resume')
        job = Jobs.objects.get(pk=job_id)
        role = job.job_role
        print(resume_file)

        applicant = Applicant(job=role, 
                              name = name,
                              email = email,
                              resume = resume_file)
        applicant.save()

        
        subject = f'New Job Application for{job.job_role}'
        body = f'A new applicant has applied for the job {job.job_role}.'
        to_email = [job.employer.email, ]
        file_path=f'{settings.MEDIA_ROOT}/applicants_resumes/{resume_file}' 
        employer_mail = EmailMessage(subject = subject,
                             body = body,
                             from_email = settings.EMAIL_HOST_USER,
                             to = to_email)
        employer_mail.attach_file(file_path)
        employer_mail.send()            

        applicant_subject = f'Successfully applied for {job.job_role} Job Application '
        body = f'Congratulations {name} you have successly applied for the job {job.job_role}.\n Wait for the response from the employer.'
        to_email = [email, ]

        applicant_mail = EmailMessage(subject = applicant_subject,
                                       body = body,
                                       from_email = settings.EMAIL_HOST_USER,
                                       to = to_email)
        applicant_mail.send()

        return render(request, 'success.html')
    



def apply(request, job_id):
    job = Jobs.objects.get(pk=job_id)
    return render(request, 'job_apply.html', {'job': job})    