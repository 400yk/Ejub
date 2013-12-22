from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse

def home(request):
    context = RequestContext(request)
    return render_to_response('ej/home.html', context)
