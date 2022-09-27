from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.about_us, name='about-us'),
    path('contact-us', views.contact_us, name='contact-us'),
    path('message-dean', views.message_dean, name='message-dean'),
    path('partner-us', views.index, name='partner-us'),
    path('department/<slug>', views.department_detail, name='department-detail'),
    path('departments', views.departments_list, name='departments-list'),
    path('program', views.program_group_detail, name='program-group-detail'),
    path('program/<slug>', views.program_group_detail, name='program-group-detail'),
    path('programs', views.program_groups_list, name='program-groups-list'),
    path('publications', views.index, name='publications'),
    path('researchs', views.index, name='researchs'),
    path('student-ressources', views.student_ressources, name='student-ressources'),
]