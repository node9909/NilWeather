from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def index(request):

  jsonString = request.body
  jsonObject = json.loads(request.body)
  print(jsonObject['lat'])
  print(jsonObject['long'])

  return HttpResponse('{"test":true}')
