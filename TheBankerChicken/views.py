from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import get_object_or_404
from TheBankerChicken.models import Account
from TheBankerChicken.forms import AccountForm

#LOGIN
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html',c, RequestContext(request))

def auth_view (request):
	username = request.POST.get('username','')
	password = request.POST.get('password','')
	user = auth.authenticate(username=username, password=password)
	if user is not None:
		m = User.objects.get(username=username)
		auth.login(request,user)
		request.session['member_id'] = m.id
		return HttpResponseRedirect('/loggedIn')
	else:
		return HttpResponse("Failed: Bad username or password", status=403)

def loggedIn(request):
	return HttpResponseRedirect('/atendimento')
							 
def invalid_login(request):
	return render_to_response('login.html')

def logout(request):
	auth.logout(request)
	return render_to_response ('login.html', RequestContext(request))
#END LOGIN

def home (request):
	return render_to_response('index.html')

# def doStuff (request):
# 	if request.method == ('POST'):
# 		name =  request.POST.get('name')
# 		selected_account = get_object_or_404(Account,name = name)
