from django.shortcuts import render
from .models import contactlist
from .models import contactform

# Create your views here.


def contactus(request):
    if request.method == 'POST':
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_subject = request.POST.get('subject')
        contact_message = request.POST.get('message')
        
        contactformdata = contactform(name=contact_name, email=contact_email, subject=contact_subject, message=contact_message)
        contactformdata.save()
    
    contactlistdata = contactlist.objects.all()[0]
    context = {
        'contactlist':contactlistdata,
    }
    return render(request, 'contact.html', context)