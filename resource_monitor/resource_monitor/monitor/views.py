from audioop import avg
from django.shortcuts import render
from .rm import *
import json
#from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
#from django.views.decorators.http import require_POST
# Create your views here.

context = {}
context['cpu'], context['avgload'], context['memory'], context

def monitor(request):
    return render(request, 'monitor/monitor.html')

#@csrf_exempt
#@require_POST
#def webhook_endpoint(request):
#    jsondata = request.body
#    data = json.loads(jsondata)
#    for answer in data['form_response']['answers']: # go through all the answers
#      type = answer['type']
#      print(f'answer: {answer[type]}') # print value of answers
#
#    return HttpResponse(status=200)