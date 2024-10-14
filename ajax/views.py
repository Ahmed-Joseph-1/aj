from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
#import json

# Create your views here.
def index(request):
	context = {}
	if request.method == "POST":
		#data = json.loads(request.body)
		Contact(
			name=request.POST['name'],
			email=request.POST['email'],
			subject=request.POST['subject'],
			message=request.POST['message'],
			ip=request.META['REMOTE_ADDR'],
			details=request.META['HTTP_USER_AGENT'],
		).save()
		
		context.update({'contact': True})
		#return HttpResponseRedirect('/#contact')
		
	return render(request, 'ajax/index.html', context)

def about(request):
	return render(request, 'ajax/about.html')
	
def terms(request):
	return render(request, 'ajax/terms.html')
	
def privacy(request):
	return render(request, 'ajax/privacy.html')

