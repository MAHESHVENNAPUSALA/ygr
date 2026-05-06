from django.urls import path
from django.contrib.auth.views import LogoutView
from django.contrib.sitemaps.views import sitemap   # ✅ CORRECT IMPORT
from . import views
from main.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [

    # ================= HOME =================
    path("", views.home, name="home"),
    path("demo/", views.demo, name="demo"),
    path("header/", views.header, name="header"),
    path("footer/", views.footer, name="footer"),
    path("services/", views.services, name="services"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("careers/", views.careers, name="careers"),
    path("contact/", views.contact, name="contact"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

    # ================= STATIC PAGES =================
    path("terms/", views.terms, name="terms"),
    path("privacy/", views.privacy, name="privacy"),
    path("cookies/", views.cookies, name="cookies"),
    path("help/", views.help, name="help"),
    path("faqs/", views.faqs, name="faqs"),
    path("refund/", views.refund, name="refund"),
    path("shipping/", views.shipping, name="shipping"),


    # ================= CAROUSEL DASHBOARD =================
    path("dashboard/carousel/", views.carousel_dashboard, name="carousel_dashboard"),
    path("dashboard/carousel/add/", views.carousel_create, name="carousel_create"),
    path("dashboard/carousel/edit/<int:id>/", views.carousel_edit, name="carousel_edit"),
    path("dashboard/carousel/delete/<int:id>/", views.carousel_delete, name="carousel_delete"),


    # ================= PROJECTS =================
    path("projects/", views.project_list, name="project_list"),
    path("projects/admin/", views.admin_project_list, name="admin_project_list"),
    path("projects/add/", views.project_add, name="project_add"),
    path("projects/<int:id>/edit/", views.project_edit, name="project_edit"),
    path("projects/<int:id>/delete/", views.project_delete, name="project_delete"),


    # ================= BLOG =================
    path("blogs/", views.blog_list, name="blog_list"),
    path("dashboard/blogs/", views.admin_blog_list, name="admin_blog_list"),
    path("dashboard/blogs/add/", views.add_blog, name="add_blog"),
    path("dashboard/blogs/edit/<int:blog_id>/", views.edit_blog, name="edit_blog"),
    path("dashboard/blogs/delete/<int:blog_id>/", views.delete_blog, name="delete_blog"),


    # ================= TEAM =================
    path("team/", views.team_list, name="team_list"),
    path("dashboard/team/", views.team_dashboard, name="team_dashboard"),
    path("dashboard/team/add/", views.team_create, name="team_create"),
    path("dashboard/team/edit/<int:id>/", views.team_edit, name="team_edit"),
    path("dashboard/team/delete/<int:id>/", views.team_delete, name="team_delete"),


    # ================= EVENTS =================
    path("dashboard/event/add/", views.event_create, name="event_create"),
    path("dashboard/event/delete/<int:id>/", views.event_delete, name="event_delete"),


    # ================= TESTIMONIALS =================
    path("dashboard/testimonials/", views.admin_testimonial_list, name="admin_testimonial_list"),
    path("dashboard/testimonials/add/", views.testimonial_create, name="testimonial_create"),
    path("dashboard/testimonials/edit/<int:pk>/", views.testimonial_update, name="testimonial_update"),
    path("dashboard/testimonials/delete/<int:pk>/", views.testimonial_delete, name="testimonial_delete"),


    # ================= USER AUTH =================
    path("login/", views.login_view, name="login"),
    path("logout/", LogoutView.as_view(next_page="careers"), name="logout"),
    path("dashboard/", views.user_dashboard, name="dashboard"),


    # ================= EXAM =================
    path("exam/", views.exam_page, name="exam_page"),
    path("exam/success/", views.exam_success, name="exam_success"),
    path("start_exam/", views.start_exam, name="start_exam"),
    path("save-answer/", views.save_answer, name="save_answer"),
    path("submit_exam/", views.submit_exam, name="submit_exam"),


    # ================= QUESTIONS =================
    path("create-question/", views.create_question_page, name="create_question_page"),
    path("save-question/", views.save_question, name="save_question"),
    path("get-questions/", views.get_questions, name="get_questions"),
    path("update-question/<int:id>/", views.update_question, name="update_question"),
    path("delete-question/<int:id>/", views.delete_question, name="delete_question"),
    path("view-questions/", views.view_questions, name="view_questions"),
    path('registers/', views.register_page, name='registers'),
    path('create-payment/', views.create_payment, name='create_payment'),
    path('payment-success/<int:reg_id>/', views.payment_success, name='payment_success'),

    path('dashboard/', views.student_dashboard, name='student_dashboard'),

    # ✅ Invoice Download
    path('invoice/<int:reg_id>/', views.download_invoice, name='download_invoice'),

    # ================= PAYMENT =================
    path("api/create-order/", views.create_order, name="create_order"),
    path("api/verify-payment/", views.verify_payment, name="verify_payment"),
    path("api/razorpay-webhook/", views.razorpay_webhook),
    path("api/payment-status/", views.payment_status, name="payment-status"),
    path("payment-success/", views.PaymentSuccessView.as_view(), name="payment-success"),
    path("api/delete-pending-user/", views.delete_pending_user),


    # ================= INTERNSHIPS ================= 
    path("internships/", views.internships_view, name="internships"),
    path("internships_list/", views.internships_list, name="internships_list"),
    path("profile/", views.profile, name="profile"),
    path("edit_profile/<int:id>/", views.edit_profile, name="edit_profile"),
    path("register/<int:course_id>/", views.register_view, name="register"),
    path('create-payment/', views.create_payment, name='create_payment'),
path('payment_success/<int:reg_id>/', views.payment_success, name='payment_success'),

    # ================= ADMIN DATA =================
    path("getdata/", views.get_data, name="get_data"),
    path("vacancies/", views.vacancies, name="vacancies"),


    # ================= ADMIN AUTH ================= 
    path("admin-login/", views.admin_login, name="admin_login"),
    path("admin-logout/", views.admin_logout, name="admin_logout"),


    # ================= ADMIN DASHBOARD =================
    path("admin-base/", views.admin_base, name="admin_base"),

    # internship dashboard

    path("internship-dashboard/", views.internship_dashboard, name="internship_dashboard"),
    path("internship-edit/<int:id>/", views.internship_edit, name="internship_edit"),
    path("internship-delete/<int:id>/", views.internship_delete, name="internship_delete"),
path("profile/download_certificate/<int:user_id>/", views.download_certificate, name="download_certificate"),

    # user admin dashboard

    path("internship_users_dashboard/", views.internship_users_dashboard, name="internship_users_dashboard"),
    path("user-profile/<int:id>/", views.user_profile, name="user_profile"),
    path("delete-user/<int:id>/", views.delete_user, name="delete_user"),

    # vacancies
     
    path("vacancies/", views.vacancies, name="vacancies"),
    path("dashboard/vacancies/", views.admin_vacancies, name="admin_vacancies"),
    path("dashboard/vacancy/add/", views.add_vacancy, name="add_vacancy"),
    path("dashboard/vacancy/edit/<int:id>/", views.edit_vacancy, name="edit_vacancy"),
    path("dashboard/vacancy/delete/<int:id>/", views.delete_vacancy, name="delete_vacancy"),

    # job applications
    path("apply/<int:job_id>/", views.job_application, name="job_application"),   
    path("my-jobs/", views.user_job_dashboard, name="user_job_dashboard"),
    path("job-login/", views.job_applicant_login, name="job_applicant_login"), 
    path('dashboard/job_application/update-status/', views.update_job_application_status, name='update_job_application_status'),
   
    path("apply/course/", views.coures, name="apply_course"),        
    path("apply/success/", views.application_success, name="application_success"),
    path("dashboard/job_applications/", views.job_applications_dashboard, name="job_applications_dashboard"),
    path("dashboard/job_application/<int:id>/", views.view_job_application, name="view_job_application"),
    path("dashboard/job_application/<int:id>/download_resume/", views.download_resume, name="download_resume"),
    path('applications/delete/<int:id>/', 
     views.delete_job_application, 
     name='delete_job_application'),


     path('blog/<int:id>/', views.blog_detail, name='blog_detail')

]