from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests


@csrf_exempt
def index(request):

  jsonString = request.body
  jsonObject = json.loads(request.body)
  lat = jsonObject['lat']
  lng = jsonObject['long']

  url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=' + lat + '&lon=' + lng
  response = requests.get(url = url)
  data = response.json()

  return HttpResponse(json.dumps(data))
