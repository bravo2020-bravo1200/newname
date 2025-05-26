from django.template import loader
from django.http import HttpResponse
from .models import Staff_member


def members(request):
    mystaff_members = Staff_member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mystaff_members': mystaff_members,
    }
    return HttpResponse(template.render(context, request))
# Create your views here.
def details(request, slug):
    mystaff_member = Staff_member.objects.get(slug=slug)
    template = loader.get_template('details.html')
    context = {
        'mystaff_member': mystaff_member,
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())
def testing(request):
    mydata = Staff_member.objects.all().order_by('id').values()
    template = loader.get_template('template.html')
    context = {
    'mystaff_members': mydata,
        
    }
    return HttpResponse(template.render(context, request))