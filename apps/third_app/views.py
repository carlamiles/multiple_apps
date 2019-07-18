from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    print('*'*50)
    print('the index method is working')
    return HttpResponse('placeholder for users to create a new user record')

def login(request):
    print('*'*50)
    print('the login method is working')
    return HttpResponse('placeholder for users to log in')

def users(request):
    print('*'*50)
    print('the user method is working')
    return HttpResponse('placeholder to later display all the list of users')

