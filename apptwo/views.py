from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes, parser_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.parsers import JSONParser

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