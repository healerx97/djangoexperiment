from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, parser_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.parsers import JSONParser


#testing csv read, write
import csv


jsonobj = {
    "glossary": {
        "title": "example glossary",
		"GlossDiv": {
            "title": "S",
			"GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
					"SortAs": "SGML",
					"GlossTerm": "Standard Generalized Markup Language",
					"Acronym": "SGML",
					"Abbrev": "ISO 8879:1986",
					"GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
						"GlossSeeAlso": ["GML", "XML"]
                    },
					"GlossSee": "markup"
                }
            }
        }
    }
}
# Create your views here.

def sample_view(*args, **kwargs):
    return HttpResponse('<h1>Hello World</h1>')

@api_view(('GET',))
@parser_classes([JSONParser])
def sample_json_res(*args, **kwargs):
    return Response(jsonobj)

@api_view(('GET',))
@parser_classes([JSONParser])
def sample_csv_res(*args, **kwargs):
    with open('sample.csv', 'w') as file:
        f = csv.writer(file)
        f.writerow(["one", "two", "three"])
        f.writerow([1,2,3])
        file.flush()
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="sample.csv"'},
    )
    return response