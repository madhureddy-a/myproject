from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Book
from .forms import contactForm
#import pdb
#import pudb

# Create your views here.

def test_view(request):
	return HttpResponse("This is sample Response")



def test_extends_parent(request):
	return render(request,'parent.html')

def test_extends_child(request):
	return render(request,'child.html')


def test_get(request):
	#pdb.set_trace()
	book_id = request.GET['book_id']
	obj = Book.objects.filter(id=book_id)
	if obj:
		obj=obj[0]
		return HttpResponse(obj.book)
	else:	
		return HttpResponse("Book with given book_id=%s found" %book_id)

def test_post(request):
	#pudb.set_trace()
	if request.method=='GET':
		return render(request,'post.html')
	else:
		name = request.POST['username']
		return HttpResponse(name)

def detail_post(request):
	#pudb.set_trace()
	if request.method=='GET':
		return render(request,'detail.html')
	else:
		name = request.POST['fname']
		return HttpResponse (name)


def home_post(request):
	if request.method == 'GET':
		form = contactForm()
		return render(request, 'home.html', {'form': form})


def form_post(request):
	if request.method=='GET':
		return render(request,'form.html')
	else:
		fname=request.POST['fname']
		lname=request.POST['lname']
		address=request.POST['address']
		age=request.POST['age']
		mobile=request.POST['mobile']
		return	render(request,'dict_form.html',context={'data':
{'first_name':fname,'last_name':lname,'address':address,'age':age,'mobile':mobile}})


		
		


		