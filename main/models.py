from django.db import models
from django.contrib.auth.models import AbstractUser

class AddCarouselImages(models.Model):
    carouseltitle=models.CharField(max_length=255)
    carouselDesc=models.CharField(max_length=255,blank=True,null=True)
    carouselImage = models.ImageField(upload_to='carousel_images/') 

class Project(models.Model):
    name = models.CharField(max_length=200)
    time_taken = models.CharField(max_length=100)
    link = models.URLField()
    image1 = models.ImageField(upload_to='projects/')
    image2 = models.ImageField(upload_to='projects/')
    image3 = models.ImageField(upload_to='projects/', blank=True, null=True)
    image4 = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.name
        
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blog_images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings  

class Internships(models.Model):
    # users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=100,blank=True,null=True)
    image=models.ImageField(upload_to='image/',blank=True,null=True)
    duration = models.CharField(max_length=100,blank=True,null=True)
    description = models.TextField(max_length=100,blank=True,null=True)
    syllabus=models.CharField(max_length=1000,blank=True,null=True)
    # âœ… New field to store completed/ticked topics by admin
    completed_topics = models.JSONField(default=list, blank=True, null=True)
    def __str__(self):
        return self.title

class User(AbstractUser):
    email = models.EmailField(max_length=50)
    phone = models.CharField(blank=True, null=True, max_length=12)
    wnumber = models.CharField(blank=True, null=True, max_length=12)
    clg_name = models.CharField(max_length=50)
    clg_address = models.CharField(max_length=100, blank=True)
    roll_no = models.CharField(max_length=20, blank=True)
    branch = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to='img/', blank=True, null=True)
    resume = models.FileField(upload_to='doc/', blank=True, null=True)
    exam_attpemt=models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)   # ðŸ”‘
    razorpay_order_id = models.CharField(max_length=100, blank=True, null=True)
    course=models.ForeignKey(Internships,on_delete=models.CASCADE,null=True,blank=True)
    

    def __str__(self):
        return f"{self.username} - {self.phone}"


#  exams---sections -------
#       
from django.db import models


class Question(models.Model):
    LANGUAGE_CHOICES = [
        ('aptitude', 'Aptitude'),
        ('reasoning', 'Reasoning'),
        ('technical', 'Technical'),
    ]

    language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES)
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1)

    def _str_(self):
        return f"{self.language} - {self.question_text[:50]}"
    



class UserAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1)  # 'A', 'B', 'C', or 'D'
    submitted_at = models.DateTimeField(auto_now=True)
    
class Score(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    score=models.IntegerField(blank=True,null=True)


# models.py
class ExamSession(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=64, unique=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended = models.BooleanField(default=False)

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150)
    country = models.CharField(max_length=50)
    message = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} - {self.company_name}"

from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
from django.db import models

 
# models.py
class LastMonthEvent(models.Model):
    image = models.ImageField(upload_to='events/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event {self.id}"


from django.db import models
from django.contrib.auth.hashers import make_password, check_password, identify_hasher


class AdminAccount(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        """Hash and set the password."""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        """Check hashed password."""
        return check_password(raw_password, self.password)

    def save(self, *args, **kwargs):
        """
        Ensure password is hashed before saving.
        Avoids double-hashing already hashed passwords.
        """
        try:
            identify_hasher(self.password)
        except Exception:
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

# vacancies 
class JobVacancy(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    package = models.CharField(max_length=100)
    description = models.TextField()
    requirements = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
         
    
from django.db import models
from django.conf import settings


class JobApplication(models.Model):
 
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="job_applications"
    )
 
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    current_city = models.CharField(max_length=100)
    current_address = models.TextField()
    permanent_address = models.TextField()
 
    job_role = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=50)

    preferred_work_mode = models.CharField(max_length=50)
    preferred_job_location = models.CharField(max_length=100)
 
    highest_qualification = models.CharField(max_length=100)
    college_university = models.CharField(max_length=200)
    passout_year = models.IntegerField()
    course = models.CharField(max_length=100)

    ssc_marks = models.CharField(max_length=10)
    inter_diploma_marks = models.CharField(max_length=10)
    higher_education_marks = models.CharField(max_length=10, blank=True, null=True)
    backlogs = models.IntegerField(blank=True, null=True)
 
    primary_skills = models.CharField(max_length=200)
    secondary_skills = models.CharField(max_length=200, blank=True, null=True)
    technical_skills = models.TextField()

    certifications = models.CharField(max_length=200, blank=True, null=True)
    internship_details = models.TextField(blank=True, null=True)
 
    candidate_type = models.CharField(max_length=50)

    total_experience = models.CharField(max_length=50, blank=True, null=True)
    relevant_experience = models.CharField(max_length=50, blank=True, null=True)

    current_company = models.CharField(max_length=100, blank=True, null=True)
    current_designation = models.CharField(max_length=100, blank=True, null=True)

    current_ctc = models.CharField(max_length=50, blank=True, null=True)
    expected_ctc = models.CharField(max_length=50, blank=True, null=True)

    notice_period = models.IntegerField(blank=True, null=True)
    reason_for_job_change = models.TextField(blank=True, null=True)
 
    resume = models.FileField(upload_to="documents/resumes/")
    profile_photo = models.ImageField(upload_to="documents/photos/")

    pan_number = models.CharField(max_length=20)
    pan_card_image = models.ImageField(upload_to='documents/pan/', blank=True, null=True)
    aadhaar_number = models.CharField(max_length=20)
    aadhaar_front_image = models.ImageField(upload_to='documents/aadhaar/', blank=True, null=True)
    aadhaar_back_image = models.ImageField(upload_to='documents/aadhaar/', blank=True, null=True) 
 
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
 
    submitted_at = models.DateTimeField(auto_now_add=True)
 
    STATUS_CHOICES = [
        ("screening", "Screening in Progress"),
        ("shortlisted", "Shortlisted"),
        ("assessment", "Online Assessment"),
        ("hr_interview", "HR Interview"),
        ("technical_interview", "Technical Interview"),
        ("documentation", "Document Verification"),
        ("onboarding", "Onboarding"),
        ("not_selected", "Not Selected"),
    ]

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="screening"
    )
 
    basic_test_date = models.DateField(blank=True, null=True)
    test_link = models.URLField(blank=True, null=True)
    document_verification_date = models.DateField(null=True, blank=True)
    interview_date = models.DateField(blank=True, null=True)
    interview_link = models.URLField(blank=True, null=True)
 
    technical_round_date = models.DateField(blank=True, null=True)
    technical_round_link = models.URLField(blank=True, null=True)
 
    document_submission_date = models.DateField(blank=True, null=True)
    join_date = models.DateField(blank=True, null=True)

    rejection_message = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
 
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job_role}"


from django.utils import timezone
from datetime import timedelta
from .models import JobApplication
from django.contrib.auth import get_user_model

User = get_user_model()

def delete_old_rejected_users():
    """Delete applications with 'not_selected' older than 90 days, and their users."""
    apps_to_delete = JobApplication.objects.filter(
        status="not_selected",
        submitted_at__lte=timezone.now() - timedelta(days=90)
    )

    for app in apps_to_delete:
        user = app.user
        app.delete()
        if user and not user.job_applications.exists():
            user.delete()
    


from django.db import models

class InternshipRegistration(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    course = models.CharField(max_length=100)
    address = models.TextField(null=True, blank=True)

    plan = models.CharField(max_length=50)

    base_amount = models.FloatField()
    gst_amount = models.FloatField()
    total_amount = models.FloatField()

    payment_type = models.CharField(max_length=20)
    emi_part = models.IntegerField(null=True, blank=True)

    razorpay_order_id = models.CharField(max_length=255)
    amount_paid = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    registration = models.ForeignKey(
        InternshipRegistration,
        on_delete=models.CASCADE
    )

    amount = models.FloatField()
    emi_part = models.IntegerField(null=True, blank=True)

    razorpay_order_id = models.CharField(max_length=200)
    razorpay_payment_id = models.CharField(max_length=200, blank=True)
    razorpay_signature = models.CharField(max_length=300, blank=True)

    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.registration.name} - ₹{self.amount}"