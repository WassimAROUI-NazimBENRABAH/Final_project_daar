from elasticsearch import Elasticsearch
#from utils import *
import json
import nltk
import json
import re




#print(ind)
# response = elastic.index(index='pdf', doc_type='pdfs', document=ind)
# print(response)


def extract_titles(txt):
    title = []
    for sent in nltk.sent_tokenize(txt):
        
        if "Title" in sent:
            title=sent.split('Title: ')[1].split('\n')[0]

    return title

def extract_author(txt):
    author=""
    for sent in nltk.sent_tokenize(txt):
       if ("Author" in sent):
        author=sent.split("Author:")[1].split("\n")[0]
        break
    return author
def extract_id(txt):
    id=""
    for sent in nltk.sent_tokenize(txt):
       if ("[eBook" in sent):
        id=sent.split("#")[1].split("]")[0]
        break
    return id

def text_json(txt):
    dict={"title": extract_titles(txt),"author": extract_author(ind),"Id":extract_id(txt),"content": txt}
    return json.dumps(dict)

elastic=Elasticsearch(hosts=["127.0.0.1"])
for i in range (67020,67037):
    print(str(i))
    f=open("pg"+str(i)+".txt","r",encoding="utf8")
    ind=f.read()
    print(extract_author(ind))
    response = elastic.index(index='pdf', doc_type='pdfs', document=text_json(ind))
    print(response)