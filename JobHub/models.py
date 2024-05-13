import uuid
from django.db import models

class Employer(models.Model):
    employer_id = models.CharField(max_length=10, unique=True, null=True, default=None)
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=128)  # Use Django's password hashing
    role = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        if not self.employer_id:
            self.employer_id = uuid.uuid4().hex[:10]  # Generate a random unique ID
        super().save(*args, **kwargs)

   

class Jobs(models.Model):
    job_role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    description = models.TextField(null=True, default='')
    date_of_publish = models.DateField(auto_now_add=True)
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, to_field='employer_id', null=True)

    def __str__(self):
        return self.job_role

    
class JobSeeker(models.Model):
    username = models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    password = models.CharField(max_length=12)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.username

class Applicant(models.Model):
    job = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='applicants_resumes')    
    