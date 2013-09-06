import os
from django.http import HttpResponse
# from django.shortcuts import render_to_response, get_object_or_404,redirect
# from django.template import RequestContext




SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

def pdf_view():
	with open(os.path.join(SITE_ROOT,'XiaoWei_ResumeCS_9_6.pdf'),'rb') as pdf:
		response = HttpResponse(pdf.read(), mimetype='application/pdf')
		print response

pdf_view()