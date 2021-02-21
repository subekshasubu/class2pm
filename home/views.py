from django.shortcuts import render
from .models import Contact
from .models import ContactInformation,Testomonials,Servicesinfo

# Create your views here.
def home(request):
    view ={}
    view['feedback'] = Testomonials.objects.all()

    return render(request,'index.html',view)

def about(request):
    return render(request,'about.html')

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def service(request):
    view={}
    view['facilities'] = Servicesinfo.objects.all()
    return render(request,'services.html',view)

def contacts(request):
    view = {}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        data = Contact.objects.create(
            full_name = name,

            email = email,
            subject = subject,
            message = message



        )
        data.save()
        view['success'] = " The Message is Submitted."


    view['info'] = ContactInformation.objects.all()




    return render(request,'contact.html',view)

