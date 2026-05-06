from django.contrib import admin
from django.utils.html import format_html
from .models import *
 
class AddCarouselImagesAdmin(admin.ModelAdmin):
    list_display = ('carouseltitle', 'carouselDesc', 'carousel_image_preview')
    search_fields = ('carouseltitle', 'carouselDesc')
    list_filter = ('carouseltitle',)
    ordering = ('carouseltitle',)
 
    def carousel_image_preview(self, obj):
        if obj.carouselImage:
            return format_html('<img src="{}" style="height: 100px;"/>', obj.carouselImage.url)
        return "-"
    carousel_image_preview.short_description = 'Image Preview'
 
admin.site.register(AddCarouselImages, AddCarouselImagesAdmin)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'created_at')



from django.contrib import admin
from .models import User,Question,UserAnswer,Score, ExamSession,Internships

# Register your models here.
admin.site.register(User)


admin.site.register(UserAnswer)
admin.site.register(Score)


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("id", "language", "question_text", "correct_option")


admin.site.register(ExamSession)
admin.site.register(Internships)


from django.contrib import admin
from .models import AdminAccount

@admin.register(AdminAccount)
class AdminAccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'is_active', 'created_at')
    search_fields = ('name', 'email')
    list_filter = ('is_active', 'created_at')
    
from django.contrib import admin
from django.utils.html import format_html
from .models import JobApplication

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    # Fields displayed in the list view
    list_display = (
        'first_name', 'last_name', 'email', 'phone', 
        'job_role', 'candidate_type', 'total_experience', 'status', 'submitted_at'
    )
    
    # Filters in the sidebar
    list_filter = (
        'job_role', 'candidate_type', 'employment_type', 
        'preferred_work_mode', 'status', 'submitted_at'
    )
    
    # Fields searchable in admin
    search_fields = (
        'first_name', 'last_name', 'email', 'phone', 
        'job_role', 'college_university'
    )
    
    # Ordering
    ordering = ('-submitted_at',)
    
    # Read-only fields
    readonly_fields = ('submitted_at',)

    # Field grouping in detail view
    fieldsets = (
        ('Personal Information', {
            'fields': (
                'first_name', 'last_name', 'dob', 'gender', 'phone', 'email',
                'current_city', 'current_address', 'permanent_address'
            )
        }),
        ('Job Information', {
            'fields': (
                'job_role', 'department', 'employment_type', 
                'preferred_work_mode', 'preferred_job_location'
            )
        }),
        ('Education', {
            'fields': (
                'highest_qualification', 'college_university', 'passout_year', 'course',
                'ssc_marks', 'inter_diploma_marks', 'higher_education_marks', 'backlogs'
            )
        }),
        ('Skills & Certifications', {
            'fields': (
                'primary_skills', 'secondary_skills', 'technical_skills', 
                'certifications', 'internship_details'
            )
        }),
        ('Experience', {
            'fields': (
                'candidate_type', 'total_experience', 'relevant_experience', 
                'current_company', 'current_designation', 'current_ctc', 
                'expected_ctc', 'notice_period', 'reason_for_job_change'
            )
        }),
        ('Documents', {
            'fields': (
                'resume', 'profile_photo', 'pan_number', 'pan_card_image', 
                'aadhaar_number', 'aadhaar_front_image', 'aadhaar_back_image'
            )
        }),
        ('Links', {
            'fields': ('linkedin', 'github')
        }),
        ('Status & Assessment', {
            'fields': (
                'status', 'basic_test_date', 'test_link', 'document_verification_date',
                'interview_date', 'interview_link', 'technical_round_date', 
                'technical_round_link', 'document_submission_date', 'join_date',
                'rejection_message', 'note'
            )
        }),
        ('Timestamps', {'fields': ('submitted_at',)}),
    )

    # Show profile photo preview in admin
    def profile_photo_preview(self, obj):
        if obj.profile_photo:
            return format_html('<img src="{}" width="50" height="50" />', obj.profile_photo.url)
        return "-"
    profile_photo_preview.short_description = 'Profile Photo'





from django.contrib import admin
from .models import InternshipRegistration, Payment


@admin.register(InternshipRegistration)
class InternshipAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'plan', 'total_amount', 'payment_type']
    search_fields = ['name', 'email']
    list_filter = ['plan', 'payment_type']


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['registration', 'amount', 'emi_part', 'is_paid', 'created_at']
    list_filter = ['is_paid']