from django.shortcuts import render
from myapp.models import Contact
# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        desc = request.POST['desc']
        values = Contact(name=name, email=email, desc=desc)
        values.save()
    return render(request, 'contact.html')
