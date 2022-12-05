from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .serializers import StudentSerializer

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        parsed_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=parsed_data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            res_msg={
                'msg':'Data was successfully saved',
            }
            json_data=JSONRenderer().render(res_msg)
            print(res_msg)
            return HttpResponse(json_data,content_type="application/json")
        else:
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type="application/json")

    return HttpResponse({"name":"Hello world"},content_type="application/json")

