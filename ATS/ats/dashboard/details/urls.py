from django.urls import path

from . import views

urlpatterns = [
    path('', views.details, name='details'),
    path('excel/', views.excel, name='excel'),
    path('loginval/', views.login_val, name='login_val'),
    path('option/',views.option,name='option'),
    path('formsubmit/',views.add_candidate,name='add_candidate'),

    path('signup/', views.signup, name='signup'),
    path('submit/', views.Stu_data, name='Stu_data'),
    path('candidates/', views.candidate_list, name='candidate_list'),
    path('candidates/excel1/', views.candidate_list_excel, name='candidate_list_excel'),
]