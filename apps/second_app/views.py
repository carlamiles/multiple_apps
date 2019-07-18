from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print('*'*50)
    print('the surveys route is working')
    return HttpResponse('placeholder to display all the surveys created')

def new(request):
    print('*'*50)
    print('the surveys route is working')
    return HttpResponse('placeholder for users to add a new survey')

