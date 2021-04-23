from django.urls import path
from student.api.views import api_detail_student_record,api_create_student_record,api_delete_student_record,api_update_student_record

app_name = "student"

urlpatterns = [

    path('<int:student_id>/',api_detail_student_record,name = "detail"),
    path('create/',api_create_student_record,name = "create"),
    path('update/<int:student_id>/',api_update_student_record,name = "update"),
    path('delete/<int:student_id>/',api_delete_student_record,name = "delete"),
    
]
