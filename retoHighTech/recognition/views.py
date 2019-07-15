from django.shortcuts import render
from django.http import HttpResponse
import boto3
from django.views.decorators.csrf import csrf_exempt
import json




# Create your views here.

def home(request):
    return render(request, template_name='recognition/index.html')


@csrf_exempt
def procesarFoto(request):
    rek = boto3.client('rekognition')
    response = rek.detect_faces(
        Image={
            'S3Object': {
                'Bucket': 'faces.demo.htsoft',
                'Name': 'fotosAI/fotoReto1.jpg',
            }
        },
        Attributes=[
            'ALL',
        ]
    )
    context=response['FaceDetails'][0]['Emotions']
    return HttpResponse(json.dumps(context))
