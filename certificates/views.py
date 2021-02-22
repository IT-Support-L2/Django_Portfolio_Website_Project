from django.shortcuts import render
from .models import IT_Certificate
from .models import DMarketing_Certificate
from .models import WebDev_Certificate

def it_certif(request):
    it_certificates = IT_Certificate.objects
    return render(request, 'certificates/information.technology.html', {'it_certificates':it_certificates})
    

def dmarketing_certif(request):
    dmarketing_certificates = DMarketing_Certificate.objects
    return render(request, 'certificates/digital.marketing.html', {'dmarketing_certificates':dmarketing_certificates})
    
def webdev_certif(request):
    webdev_certificates = WebDev_Certificate.objects
    return render(request, 'certificates/web.development.html', {'webdev_certificates':webdev_certificates})
    