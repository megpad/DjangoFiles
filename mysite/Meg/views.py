'''from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	message = "Hello, Meg"
	return HttpResponse(message)

def page(request, page_id):
	if page_id == 1:
		message = "ページ１"
	else:
		message = "ページはありません"

	return HttpResponse(message)
'''

from django.http import HttpResponse
from django.template import loader

from.models import Article

def article(request):
	template = loader.get_template('article.html')
	context = {
		'title': "記事のタイトル",
		"content": "記事の本文"
	}
	return HttpResponse(template.render(context, request))

# Create your views here.
