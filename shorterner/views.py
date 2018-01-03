from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent
from .models import KirrURL
from .forms import SubmitUrlForm
# Create your views here.

# def home_view_fbv(request, *args, **kwargs):
# 	if request.method == "POST":
# 		print(request.POST)
# 	return render(request, "kirr/main.html", {})

class HomeView(View):
	def get(self, request, *args, **kwargs):
		the_form = SubmitUrlForm()
		#context = {
		#	'title': 'Submit URLS',
		#	'form' : the_form
		#}
		return render(request, "kirr/main.html", {"title":"title","form":the_form}) #Try django 1.9 and 1.9 http://joincfe.com/youtube

	def post(self, request, *args, **kwargs):
		#print(request.POST)
		print(request.POST.get('url'))
		form = SubmitUrlForm(request.POST)
		context = {
			'title': 'Submit URLS',
			'form' : form
		}
		template = 'kirr/main.html'
		if form.is_valid():
			new_url = form.cleaned_data.get('url')
			obj, created = KirrURL.objects.get_or_create(url=new_url)
			context = {
				'object': obj,
				'created': created,
			}
			if created:
				template = 'kirr/success.html'
			else:
				template = 'kirr/already-exists.html'
		
		return render(request, template, context)

#def kirr_redirect_view(request, title=None, *args, **kwargs): #function based view FBV
#	obj = get_object_or_404(KirrURL, shortcode=title)
#	return HttpResponseRedirect(obj.url)
#	#return HttpResponse("sa to {t}".format(t=obj.url))


class URLRedirectView(View): #class based view CBV
	def get(self, request, shortcode=None, *args, **kwargs):
		qs = KirrURL.objects.filter(shortcode__iexact=shortcode)
		if qs.count() == 1 and qs.exists():
			obj = qs.first()
			print(ClickEvent.objects.create_event(obj))
			return HttpResponseRedirect(obj.url)
		raise Http404
		# obj = get_object_or_404(KirrURL, shortcode=title)
		# #save item
		# print(ClickEvent.objects.create_event(obj))
		# return HttpResponseRedirect(obj.url)
		# #return HttpResponse("sa again to {t}".format(t=obj.url))

	def post(self, request, *args, **kwargs):
		return HttpResponse()


'''

def kirr_redirect_view(request, title=None, *args, **kwargs): #function based view FBV
	#print(request.user)
	#print(request.user.is_authenticated)
	#print(args)
	#obj = KirrURL.objects.get(shortcode=title)

	obj = get_object_or_404(KirrURL, shortcode=title)
	#obj_url = obj.url

	#try:
	#	obj = KirrURL.objects.get(shortcode=title)
	#except:
	#	obj = KirrURL.objects.all().first()

	#obj_url = None
	#qs = KirrURL.objects.filter(shortcode__iexact=title.upper())
	#if qs.exists() and qs.count() == 1:
	#	obj = qs.first()
	#	obj_url = obj.url

	return HttpResponse("sa to {t}".format(t=obj.url))

'''