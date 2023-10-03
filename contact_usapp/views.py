from django.shortcuts import render
from .models import Contact

def home(request):
    return render(request,'home.html')
def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        # print(name,email,message)
        # data base syntax to save the data
        data = Contact(name=name,email=email,message=message)
        data.save()

    return render(request,'contactus.html')