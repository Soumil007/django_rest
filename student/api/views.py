from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from student.models import Student
from student.api.serializers import StudentSerializer

@api_view(['GET',])
def api_detail_student_record(request,student_id):

    try:
        student_record = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = StudentSerializer(student_record)
        return Response(serializer.data)

@api_view(['PUT',])
def api_update_student_record(request,student_id):
    try:
        student_record = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = StudentSerializer(student_record,data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "update successful"
            return Response(data = data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE',])
def api_delete_student_record(request,student_id):
    try:
        student_record = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == "DELETE":
        operation = student_record.delete()
        data = {}
        if operation:
            data["successful"] = "delete successful"
        else:
            data["failure"] = "delete failed"
        return Response(data = data)

@api_view(['POST',])
def api_create_student_record(request):

    if request.method == "POST":
        serializer = StudentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



