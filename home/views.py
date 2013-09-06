# Create your views here.
import os
from django.http import HttpResponse
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


def pdf_view_cs(request):
	with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'Xiao_Wei_ResumeCS_9_6_13.pdf'),'rb') as pdf:
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'inline; filename =Xiao_Wei_ResumeCS_9_6_13.pdf'
		return response

def pdf_view_ee(request):
	with open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'Xiao_Wei_ResumeEE_9_6_13.pdf'),'rb') as pdf:
		response = HttpResponse(pdf.read(), content_type='application/pdf')
		response['Content-Disposition'] = 'inline; filename =Xiao_Wei_ResumeEE_9_6_13.pdf'
		return response

	