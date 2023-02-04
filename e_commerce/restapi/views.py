from django.shortcuts import render
from . serializer import studentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Student
from django.http import HttpResponse
import logging

# Create your views here.

logger = logging.getLogger('django')


@api_view(['POST'])
def add_student(request):
    logger.info("this is info message")
    params = request.data
    serialized_data = studentSerializer(data = params)

    if serialized_data.is_valid() :
        serialized_data.save()
        return Response({'statusCode' : 201,'msg': 'student added successfully'})

    else:
        return Response({'statusCode' : 500, 'msg': 'form error'})    


@api_view(['GET'])
def list_student(request):
    student = Student.objects.all()
    serialized_data = studentSerializer(student, many = True)
    return Response({'students' : serialized_data.data})
    
@api_view(['DELETE'])
def delete_student(request,sid):
    try:
        student = Student.objects.get(id = sid)
        student.delete()
    except:
        return Response({'statusCode' : 404,'msg': 'student Not Found'})
        
    return Response({'statusCode' : 200,'msg': 'student Delete successfully'})


@api_view(['PUT'])
def update_student(request,sid):
    params = request.data
    student = Student.objects.get(id = sid)
    serialized_data = studentSerializer(student, data = params) 

    if serialized_data.is_valid() :
        serialized_data.save()
        return Response({'statusCode' : 200,'msg': 'Data Updated Successfully'})

    else:
        return Response({'statusCode' : 500, 'msg': 'form error'})   


@api_view(['GET'])
def index(request):
    return Response('congratulations, you have created an API')


@api_view(['GET'])
def number(request):
    return Response(3.90)

