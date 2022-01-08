from django.shortcuts import render
from elk.utils import *
from django.core.files.storage import FileSystemStorage
from elasticsearch import Elasticsearch
from django.views.generic.base import TemplateView
from django.conf import settings
from django.http import HttpResponse


class Home(TemplateView):
    template_name = 'interface.html'

def search(request):
    elastic_client = Elasticsearch(hosts=["127.0.0.1"])
    if request.method == "POST":
       content=request.POST.get("content")
       if(request.POST.get("advenced")=="on"): 
            payload = json.dumps({
                "query": {
                "regexp": {
                "content": content+".*"
                }
                },
                "size": "2000"
            })
       else:
           payload = json.dumps({
                "query": {
                "match": {
                "content": content
                }
                },
                "size": "2000"
            })

    response=elastic_client.search(index="pdf", body=payload)
    li= []
    for i in response['hits']['hits']:
        l=[]
        l.append(i['_source']['title'])
        l.append(i['_source']['author'])
        l.append(i['_source']['Id'])
        li.append(l)
    return render(request, 'suggestion.html', {'resp': content,'list':li})
    

