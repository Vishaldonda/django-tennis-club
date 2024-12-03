from django.shortcuts import render # used to generate HTTP responses by rendering templates.
from django.http import HttpResponse
from . import models
import datetime

# Create your views here.
def main(request):
    return render(request,'main.html')

def members(request):
    # return HttpResponse("Hello World")    
    # render(request, 'myfirst.html', context=None, content_type=None, status=None, using=None)
    
    members = models.Members.objects.values()
    # print(members) # <QuerySet [{'id': 1, 'firstname': 'John', 'lastname': 'Doe', 'phone': 5551234, 'joined_date': datetime.date(2022, 1, 5)}, {'id': 2, 'firstname': 'Linus', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}, {'id': 3, 'firstname': 'Lene', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}]>
    
    # for member in members:
    #     print(member)
    
    return render(request, 'all_members.html', context= { 'mymembers' : members})

def details(request,id):
    
    members = models.Members.objects.get(id=id)
    
    print("here",members)
    # for member in members:
    #     print(member)
    
    
    return render(request, 'details.html', context= { 'mymembers' : members})
    

def testing(request):
    members = [{'id': 1, 'firstname': 'John', 'lastname': 'Doe', 'phone': 5551234, 'joined_date': datetime.date(2022, 1, 5)}, {'id': 2, 'firstname': 'Linus', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}, {'id': 3, 'firstname': 'Lene', 'lastname': 'Refsnes', 'phone': None, 'joined_date': None}]
    fruits = ['Apple', 'Banana', 'Cherry']
    
    # return render(request, 'template.html', context= { 'mymembers' : members})
    return render(request, 'template.html', context= { 'mymembers' : fruits})