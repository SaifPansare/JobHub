from django.contrib import admin
from .models import Employer, Jobs, JobSeeker, Applicant

class EmployerDisplay(admin.ModelAdmin):
    list_display=('username', )

class JobDisplay(admin.ModelAdmin):
    list_display=('job_role', )

class JobSeekerDisplay(admin.ModelAdmin):
    list_display=('username', )

class ApplicantDisplay(admin.ModelAdmin):
    list_display=('name', )

admin.site.register(Employer, EmployerDisplay)
admin.site.register(Jobs, JobDisplay)

admin.site.register(JobSeeker, JobSeekerDisplay)
admin.site.register(Applicant, ApplicantDisplay)
