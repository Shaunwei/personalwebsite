# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404,redirect
from django.template import RequestContext
from home.models import Resume

def home(request):
	homeinfo = Resume.objects.all()
	return render_to_response('resume.html', {'homeinfo':homeinfo})



def resume(request, re_id):
	resumeinfo = get_object_or_404(Resume,pk = re_id)
	return render_to_response('home.html', resumeinfo)

def test(request):
	homeinfo = Resume.objects.all()
	return render_to_response('resume.html',{'homeinfo':homeinfo},context_instance=RequestContext(request))


	