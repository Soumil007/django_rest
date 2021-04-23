from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from student.models import Student
# Create your views here.


def index(request):
    return HttpResponse('Hello World')

def getAllStudents(request):
    students = Student.objects.order_by('-rollno')[:4]
    output = ', '.join([s.name for s in students])
    print(output)
    return JsonResponse(output)